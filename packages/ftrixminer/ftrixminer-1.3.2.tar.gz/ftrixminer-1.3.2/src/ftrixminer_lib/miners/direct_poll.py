import asyncio
import logging
from pathlib import Path
from typing import List

import pytds
from dls_utilpack.callsign import callsign
from dls_utilpack.explain import explain2
from dls_utilpack.require import require
from dls_utilpack.visit import VisitNotFound, get_xchem_subdirectory

# Crystal plate constants.
from xchembku_api.crystal_plate_objects.constants import TREENODE_NAMES_TO_THING_TYPES

# Dataface client context.
from xchembku_api.datafaces.context import Context as XchembkuDatafaceClientContext
from xchembku_api.models.crystal_plate_filter_model import CrystalPlateFilterModel

# Crystal well pydantic model.
from xchembku_api.models.crystal_plate_model import CrystalPlateModel

# Base class for miner instances.
from ftrixminer_lib.miners.base import Base as MinerBase

logger = logging.getLogger(__name__)

thing_type = "ftrixminer_lib.miners.direct_poll"


# ------------------------------------------------------------------------------------------
class DirectPoll(MinerBase):
    """
    Object representing plate miner.
    The behavior is to start a coro task to waken every few seconds and scan for new plates.
    Files are pushed to xchembku.
    """

    # ----------------------------------------------------------------------------------------
    def __init__(self, specification, predefined_uuid=None):
        MinerBase.__init__(
            self, thing_type, specification, predefined_uuid=predefined_uuid
        )

        s = f"{callsign(self)} specification", self.specification()

        type_specific_tbd = require(s, self.specification(), "type_specific_tbd")
        self.__mssql = require(s, type_specific_tbd, "mssql")
        xchembku_dataface_specification = require(
            s, type_specific_tbd, "xchembku_dataface_specification"
        )

        # Create a dataface context objectwhere we push new plates discovered.
        self.__xchembku_client_context = XchembkuDatafaceClientContext(
            xchembku_dataface_specification
        )

        # Activate the context later.
        self.__xchembku = None

        # This flag will stop the ticking async task.
        self.__keep_ticking = True
        self.__tick_future = None

        self.__latest_formulatrix__plate__ids = ["0"]
        self.__query_count = 0

    # ----------------------------------------------------------------------------------------
    async def activate(self) -> None:
        """
        Activate the object.

        This implementation gets the list of filenames already known to the xchembku.

        Then it starts the coro task to awaken every few seconds to scrape the directories.
        """

        # Activate the context.
        await self.__xchembku_client_context.aenter()

        # Get a reference to the xchembku interface provided by the context.
        self.__xchembku = self.__xchembku_client_context.get_interface()

        # Get latest plate we already have in the database.
        # This allows us to query mssql for just plates that are newer.
        crystal_plate_models = await self.__xchembku.fetch_crystal_plates(
            CrystalPlateFilterModel(limit=100, direction=-1),
            why="latest plate we already have in the database",
        )

        for crystal_plate_model in crystal_plate_models:
            self.__latest_formulatrix__plate__ids.append(
                str(crystal_plate_model.formulatrix__plate__id)
            )

        # Poll periodically.
        self.__tick_future = asyncio.get_event_loop().create_task(self.tick())

    # ----------------------------------------------------------------------------------------
    async def deactivate(self) -> None:
        """
        Deactivate the object.

        Causes the coro task to stop.

        This implementation then releases resources relating to the xchembku connection.
        """

        if self.__tick_future is not None:
            # Set flag to stop the periodic ticking.
            self.__keep_ticking = False
            # Wait for the ticking to stop.
            await self.__tick_future

        # Forget we have an xchembku client reference.
        self.__xchembku = None

        if self.__xchembku_client_context is not None:
            await self.__xchembku_client_context.aexit()
            self.__xchembku_client_context = None

    # ----------------------------------------------------------------------------------------
    async def tick(self) -> None:
        """
        A coro task which does periodic checking for new files in the directories.

        Stops when flag has been set by other tasks.

        # TODO: Use an event to awaken ticker early to handle stop requests sooner.
        """

        while self.__keep_ticking:
            try:
                await self.discover()
            except Exception as exception:
                logger.error(explain2(exception, "scraping"), exc_info=exception)

            # TODO: Make periodic tick period to be configurable.
            await asyncio.sleep(1.0)

    # ----------------------------------------------------------------------------------------
    async def discover(self) -> None:
        """
        Scrape discover new plates in the Formulatrix database.
        """

        # Query mssql or dummy.
        rows = await self.query()

        logger.debug(f"[FTRIXMINER POLL] discovered {len(rows)} new plate rows")

        # Loop over the rows we got back from the query.
        for row in rows:
            formulatrix__plate__id = int(row[0])
            thing_type = TREENODE_NAMES_TO_THING_TYPES.get(row[3])
            if thing_type is None:
                raise RuntimeError(f"programming error: plate type {row[3]} unexpected")

            # Get a proper visit name from the formulatrix's "experiment" tree_node name.
            # The techs name the experiment tree node like sw30864-12_something,
            # and the visit is parsed out as the part before the first underscore.
            formulatrix__experiment__name = str(row[2])
            should_upsert = True
            try:
                xchem_subdirectory = get_xchem_subdirectory(
                    formulatrix__experiment__name
                )
                # The xchem_subdirectory comes out like sw30864/sw30864-12.
                # We only store the actual visit into the database field.
                visit = Path(xchem_subdirectory).name

            # Completely skip formulatrix plates with names not formatted properly as visits.
            except ValueError as exception:
                logger.warning(
                    f'ignoring plate with formulatrix__experiment__name "{formulatrix__experiment__name}" because {str(exception)}'
                )
                should_upsert = False

            # Completely skip formulatrix plates which don't have visit directories established.
            except VisitNotFound as exception:
                logger.warning(
                    f'ignoring plate with formulatrix__experiment__name "{formulatrix__experiment__name}" because {str(exception)}'
                )
                should_upsert = False

            if should_upsert:
                # Wrap a model around the attributes.
                crystal_plate_model = CrystalPlateModel(
                    visit=visit,
                    barcode=str(row[1]),
                    thing_type=thing_type,
                    formulatrix__experiment__name=formulatrix__experiment__name,
                    formulatrix__plate__id=formulatrix__plate__id,
                )

                # Add plate to our database.
                # I don't worry about performance hit of adding plates one by one with upsert
                # since new plates don't get added very often.
                await self.__xchembku.upsert_crystal_plates([crystal_plate_model])

            # Remember the latest plate id that we have examined.
            # After a restart  we lose the instance variable,
            # so we will possibly re-examine those after the final actual upsert,
            # but that's not a lot of work.
            self.__latest_formulatrix__plate__ids.append(str(formulatrix__plate__id))

    # ----------------------------------------------------------------------------------------
    async def query(self) -> List[List]:
        """
        Read dummy data from configuration.
        """

        server = self.__mssql["server"]

        if server == "dummy":
            return await self.query_dummy()
        else:
            return await self.query_mssql()

    # ----------------------------------------------------------------------------------------
    async def query_mssql(self) -> List[List]:
        """
        Scrape discover new plates in the Formulatrix database.
        """

        # Connect to the RockMaker database at every tick.
        # TODO: Handle failure to connect to RockMaker database.
        connection = pytds.connect(
            self.__mssql["server"],
            self.__mssql["database"],
            self.__mssql["username"],
            self.__mssql["password"],
        )

        # Select only plate types we care about.
        treenode_names = [
            f"'{str(name)}'" for name in list(TREENODE_NAMES_TO_THING_TYPES.keys())
        ]

        # Plate's treenode is "ExperimentPlate".
        # Parent of ExperimentPlate is "Experiment", aka visit
        # Parent of Experiment is "Project", aka plate type.
        # Parent of Project is "ProjectsFolder", we only care about "XChem"
        # Get all xchem barcodes and the associated experiment name.
        sql = (
            "SELECT"
            "\n  Plate.ID AS id,"
            "\n  Plate.Barcode AS barcode,"
            "\n  experiment_node.Name AS experiment,"
            "\n  plate_type_node.Name AS plate_type"
            "\nFROM Plate"
            "\nJOIN Experiment ON experiment.ID = plate.experimentID"
            "\nJOIN TreeNode AS experiment_node ON experiment_node.ID = Experiment.TreeNodeID"
            "\nJOIN TreeNode AS plate_type_node ON plate_type_node.ID = experiment_node.ParentID"
            "\nJOIN TreeNode AS projects_folder_node ON projects_folder_node.ID = plate_type_node.ParentID"
            f"\nWHERE Plate.ID > {self.__latest_formulatrix__plate__ids[-1]}"
            "\n  AND projects_folder_node.Name = 'xchem'"
            f"\n  AND plate_type_node.Name IN ({',' .join(treenode_names)})"
            f"\n  AND Plate.ID NOT IN ({', '.join(self.__latest_formulatrix__plate__ids)})"
        )

        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        if self.__query_count % 60 == 0:
            logger.debug(
                f"[FTRIXMINER POLL] query #{self.__query_count}. got {len(rows)} rows from\n{sql}"
            )

        self.__query_count += 1

        return rows

    # ----------------------------------------------------------------------------------------
    async def query_dummy(self) -> List[List]:
        """
        Read dummy data from configuration.
        """

        database = self.__mssql["database"]
        records = self.__mssql[database]

        # Keep only records that haven't been queried before.
        new_records = []
        for record in records:
            if record[0] not in self.__latest_formulatrix__plate__ids:
                new_records.append(record)

        return new_records

    # ----------------------------------------------------------------------------------------
    async def close_client_session(self):
        """"""

        pass

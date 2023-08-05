import logging

# Things created in the context.
from rockingester_api.collectors.collectors import (
    Collectors,
    rockingester_collectors_set_default,
)

# Base class.
from rockingester_api.context_base import ContextBase

logger = logging.getLogger(__name__)


class Context(ContextBase):
    """
    Client context for a rockingester_collector object.
    On entering, it creates the object according to the specification (a dict).
    On exiting, it closes client connection.

    The aenter and aexit methods are exposed for use by an enclosing context.
    """

    # ----------------------------------------------------------------------------------------
    def __init__(self, specification):
        self.__specification = specification

    # ----------------------------------------------------------------------------------------
    async def aenter(self):
        """ """

        # Build the object according to the specification.
        self.interface = Collectors().build_object(self.__specification)

        # If there is more than one collector, the last one defined will be the default.
        rockingester_collectors_set_default(self.interface)

    # ----------------------------------------------------------------------------------------
    async def aexit(self):
        """ """

        if self.interface is not None:
            await self.interface.close_client_session()

            # Clear the global variable.  Important between pytests.
            rockingester_collectors_set_default(None)

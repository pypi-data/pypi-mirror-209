from typing import List, Optional

import aiohttp
from aiohttp import ClientResponseError
from aiohttp.web_exceptions import HTTPNotFound

from klu.api.client import APIClient
from klu.action.models import Action
from klu.application.constants import (
    APPLICATION_ENDPOINT,
    APPLICATION_DATA_ENDPOINT,
    APPLICATION_ACTIONS_ENDPOINT,
)
from klu.common.client import KluClientBase
from klu.application.models import Application
from klu.utils.dict_helpers import dict_no_empty
from klu.common.errors import InvalidUpdateParamsError
from klu.application.errors import ApplicationNotFoundError


class ApplicationsClient(KluClientBase):
    def __init__(self, api_key: str):
        super().__init__(api_key, APPLICATION_ENDPOINT, Application)

    async def create(self, name: str, app_type: str, description: str) -> Application:
        """
        Creates new application instance

        Args:
            name: str. Name of a new application
            app_type: str. Type of a new application
            description: str. Description of a new application

        Returns: Newly created Application object
        """
        return await super().create(
            name=name,
            app_type=app_type,
            description=description,
        )

    async def get(self, guid: str) -> Application:
        """
        Retrieves app  information based on the app id.

        Args:
            guid (str): GUID of an application to fetch. The one that was used during the app creation

        Returns: Application object
        """
        return await super().get(guid)

    async def update(
        self,
        guid: str,
        name: Optional[str] = None,
        app_type: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Application:
        """
        Update application metadata. At least one of the params has to be provided

        Args:
            guid (str): GUID of an application to fetch. The one that was used during the app creation
            name: Optional[str]. New application name
            app_type: Optional[str]. New application type
            description: Optional[str]. New application description

        Returns: Updated application instance
        """

        if not name and not app_type and not description:
            raise InvalidUpdateParamsError()

        return await super().update(
            **{
                "id": guid,
                **dict_no_empty({"name": name, "app_type": app_type, "description": description}),
            }
        )

    async def delete(self, guid: str) -> Application:
        """
        Delete existing application information defined by the app id.

        Args:
            guid (str): The id of an application to delete.

        Returns: Deleted application object
        """
        return await super().delete(guid)

    async def get_app_data(self, app_guid: str) -> List[Action]:
        """
        Retrieves app actions information based on the app GUID.

        Args:
            app_guid (str): GUID of an application to fetch actions for. The one that was used during the app creation

        Returns: An array of actions, found by provided app id.
        """
        async with aiohttp.ClientSession() as session:
            client = APIClient(session, self._api_key)
            try:
                response = await client.get(APPLICATION_DATA_ENDPOINT.format(id=app_guid))
            except (HTTPNotFound, ClientResponseError) as e:
                if e.status == 404:
                    raise ApplicationNotFoundError(app_guid)

            return [Action._from_engine_format(action) for action in response]

    async def get_app_actions(self, app_guid: str) -> List[Action]:
        """
        Retrieves app actions information based on the app GUID.

        Args:
            app_guid (str): GUID of an application to fetch actions for. The one that was used during the app creation

        Returns: An array of actions, found by provided app id.
        """
        async with aiohttp.ClientSession() as session:
            client = APIClient(session, self._api_key)
            try:
                response = await client.get(APPLICATION_ACTIONS_ENDPOINT.format(id=app_guid))
            except (HTTPNotFound, ClientResponseError) as e:
                if e.status == 404:
                    raise ApplicationNotFoundError(app_guid)

            return [Action._from_engine_format(action) for action in response]

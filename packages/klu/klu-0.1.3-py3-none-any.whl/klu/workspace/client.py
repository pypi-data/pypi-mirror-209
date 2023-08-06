from typing import List

import aiohttp
from aiohttp import ClientResponseError
from aiohttp.web_exceptions import HTTPNotFound

from klu.model.models import Model
from klu.workspace.constants import (
    WORKSPACE_ENDPOINT,
    WORKSPACE_APPS_ENDPOINT,
    WORKSPACE_MODELS_ENDPOINT,
    WORKSPACE_INDICES_ENDPOINT,
)
from klu.workspace.models import Workspace
from klu.common.client import KluClientBase
from klu.data_index.models import DataIndex
from klu.application.models import Application
from klu.workspace.errors import WorkspaceOrUserNotFoundError


class WorkspaceClient(KluClientBase):
    def __init__(self, api_key: str):
        super().__init__(api_key, WORKSPACE_ENDPOINT, Workspace)

    async def create(self, name: str, slug: str) -> Workspace:
        """
        Creates a Workspace based on the data provided.

        Args:
            name (str): Model key. Required
            slug (str): Workspace slug. The unique name you would prefer to use to access the model.

        Returns: A newly created Workspace object.
        """
        return await super().create(name=name, slug=slug)

    async def get(self, guid: str) -> Workspace:
        """
        Retrieves a single workspace object by provided workspace id

        Args:
            guid (str): The ID of a workspace to fetch. project_guid you sent during the workspace creation

        Returns: A workspace object
        """
        return await super().get(guid)

    async def update(self, guid: str, name: str) -> Workspace:
        """
        Update workspace data. Currently, only name update is supported.

        Args:
            guid (str): ID of a data_index to update. project_guid you sent during the workspace creation
            name: str. New workspace name.

        Returns: Updated workspace instance
        """
        return await super().update(id=guid, name=name)

    async def delete(self, guid: str) -> Workspace:
        """
        Delete Workspace based on the id.

        Args:
            guid (str): ID of a workspace to delete. project_guid you sent during the workspace creation

        Returns: Deleted workspace object
        """
        return await super().delete(guid)

    async def list(self) -> List[Workspace]:
        """
        Retrieves the list of workspaces for currently authenticated user.

        Returns: Array of workspaces found for user
        """
        async with aiohttp.ClientSession() as session:
            client = self._get_api_client(session)
            try:
                response = await client.get(WORKSPACE_ENDPOINT)
            except (HTTPNotFound, ClientResponseError) as e:
                if e.status == 404:
                    raise WorkspaceOrUserNotFoundError()

        return [Workspace._from_engine_format(workspace) for workspace in response]

    async def get_workspace_apps(self, guid: str) -> List[Application]:
        """
        Retrieves the list of applications for workspace defined by provided guid

        Args:
            guid (str): The ID of workspace to fetch applications for.

        Returns: List of applications found in a workspace
        """
        async with aiohttp.ClientSession() as session:
            client = self._get_api_client(session)
            try:
                response = await client.get(
                    WORKSPACE_APPS_ENDPOINT.format(id=guid),
                )
            except (HTTPNotFound, ClientResponseError) as e:
                if e.status == 404:
                    raise WorkspaceOrUserNotFoundError()

            return [Application._from_engine_format(application) for application in response]

    async def get_workspace_indices(self, guid: str) -> List[DataIndex]:
        """
        Retrieves the list of data_indices for workspace defined by provided guid

        Args:
            guid (str): The ID of workspace to fetch data_indices for.
                project_guid you sent during the workspace creation

        Returns: List of DataIndex objects found on a workspace.
        """
        async with aiohttp.ClientSession() as session:
            client = self._get_api_client(session)
            try:
                response = await client.get(
                    WORKSPACE_INDICES_ENDPOINT.format(id=guid),
                )
            except (HTTPNotFound, ClientResponseError) as e:
                if e.status == 404:
                    raise WorkspaceOrUserNotFoundError()

            return [DataIndex._from_engine_format(data_index) for data_index in response]

    async def get_workspace_models(self, guid: str) -> List[Model]:
        """
        Retrieves the list of models for provided workspace id

        Args:
            guid (str): The ID of workspace to fetch models for. project_guid you sent during the workspace creation

        Returns: List of Model objects found on a workspace.
        """
        async with aiohttp.ClientSession() as session:
            client = self._get_api_client(session)
            try:
                response = await client.get(
                    WORKSPACE_MODELS_ENDPOINT.format(id=guid),
                )
            except (HTTPNotFound, ClientResponseError) as e:
                if e.status == 404:
                    raise WorkspaceOrUserNotFoundError()

            return [Model._from_engine_format(model) for model in response]

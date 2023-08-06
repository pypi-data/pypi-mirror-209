from uuid import uuid4

import pytest

from klu.client.klu import KluClient

from tests.integration.constants import API_KEY
from tests.integration.utils.data import create_data
from tests.integration.utils.actions import create_action
from tests.integration.utils.models import ModelSingleton
from tests.integration.utils.applications import create_application

client = KluClient(API_KEY)

model_singleton = ModelSingleton()


def get_test_app_name() -> str:
    return f"test-app-name-{str(uuid4())}"


@pytest.mark.asyncio
async def test_list_app_data():
    default_model = await model_singleton.get_default_model()

    app = await create_application()
    action = await create_action(app_guid=app.guid, model_guid=default_model.guid)

    await create_data(action_guid=action.guid)
    await create_data(action_guid=action.guid)

    data = await client.applications.get_app_data(app.guid)
    assert len(data) == 2


@pytest.mark.asyncio
async def test_list_app_actions():
    default_model = await model_singleton.get_default_model()

    app = await create_application()
    await create_action(app_guid=app.guid, model_guid=default_model.guid)
    await create_action(app_guid=app.guid, model_guid=default_model.guid)

    actions = await client.applications.get_app_actions(app.guid)
    assert len(actions) == 2


@pytest.mark.asyncio
async def test_crud_applications():
    test_app_name = get_test_app_name()

    create_response = await create_application(
        name=test_app_name,
        app_type="test-app-type",
        description="test-app-description",
    )

    assert create_response.name == test_app_name
    assert create_response.guid is not None
    assert create_response.created_by_id is not None

    created_instance_guid = create_response.guid
    get_response = await client.applications.get(created_instance_guid)
    assert get_response.guid == created_instance_guid

    new_app_name = f"new-test-app-name-{str(uuid4())}"
    update_response = await client.applications.update(
        created_instance_guid,
        name=new_app_name,
    )
    assert update_response.name == new_app_name

    delete_response = await client.applications.delete(created_instance_guid)
    assert delete_response.guid == created_instance_guid

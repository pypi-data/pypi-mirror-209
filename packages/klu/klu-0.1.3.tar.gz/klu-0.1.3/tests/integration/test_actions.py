import pytest

from tests.integration import client
from tests.integration.utils.data import create_data
from tests.integration.utils.models import ModelSingleton
from tests.integration.utils.applications import AppSingleton
from tests.integration.utils.actions import create_action, ActionSingleton

app_singleton = AppSingleton()
model_singleton = ModelSingleton()
action_singleton = ActionSingleton()


@pytest.mark.asyncio
async def test_run_action_prompt():
    action = await action_singleton.get_default_action()
    action_prompt_result = await client.actions.run_action_prompt(action.guid, "test", "test", False)

    assert action_prompt_result.msg
    assert action_prompt_result.streaming_url is None


@pytest.mark.asyncio
async def test_run_action_prompt_returns_streaming_url():
    action = await action_singleton.get_default_action()
    action_prompt_result = await client.actions.run_action_prompt(action.guid, "test", "test", True)
    assert action_prompt_result.streaming_url is not None


@pytest.mark.asyncio
async def test_run_playground_prompt():
    playground_prompt_result = await client.actions.run_playground_prompt("test", 1)
    assert playground_prompt_result.msg is not None


@pytest.mark.asyncio
async def test_get_action_data():
    action = await action_singleton.get_default_action()
    await create_data(action_guid=action.guid)

    action_data = await client.actions.get_action_data(action.guid)
    assert len(action_data) > 0


@pytest.mark.asyncio
async def test_crud_actions():
    default_app = await app_singleton.get_default_app()
    default_model = await model_singleton.get_default_model()

    create_response = await create_action(
        app_guid=default_app.guid,
        model_guid=default_model.guid,
    )
    action_guid = create_response.guid

    assert create_response.app_id == default_app.id
    assert create_response.model_id == default_model.id

    get_response = await client.actions.get(action_guid)
    assert get_response.guid == action_guid

    new_app_name = "new-test-app-name"
    update_response = await client.actions.update(action_guid, name=new_app_name)
    assert update_response.name == new_app_name
    delete_response = await client.actions.delete(action_guid)
    assert delete_response.guid == action_guid

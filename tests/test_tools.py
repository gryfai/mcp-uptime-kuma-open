import pytest
import json
from fastmcp import FastMCP
from fastmcp.exceptions import ToolError
from mcp_uptime_kuma_open import tools

@pytest.mark.asyncio
async def test_get_uptime_kuma_monitors(mocker):
    """
    GIVEN a FastMCP instance and a mocked service layer
    WHEN the get_uptime_kuma_monitors tool is called
    THEN it should return the mocked monitor data
    """
    # ARRANGE
    mcp = FastMCP()
    mock_data = [{"id": 1, "name": "Mock Monitor"}]
    mock_get_all_monitors = mocker.patch(
        "mcp_uptime_kuma_open.tools.get_all_monitors",
        return_value=mock_data
    )
    tools.register_tools(mcp)
    get_monitors_tool = await mcp.get_tool("get_uptime_kuma_monitors")

    # ACT
    result = await get_monitors_tool.run(arguments={})

    # ASSERT
    mock_get_all_monitors.assert_called_once()
    assert json.loads(result.content[0].text) == mock_data

@pytest.mark.asyncio
async def test_get_specific_uptime_kuma_monitor(mocker):
    """
    GIVEN a FastMCP instance and a mocked service layer
    WHEN the get_specific_uptime_kuma_monitor tool is called with an ID
    THEN it should return the specific mocked monitor data
    """
    # ARRANGE
    mcp = FastMCP()
    mock_data = {"id": 2, "name": "Specific Monitor"}
    mock_get_specific_monitor = mocker.patch(
        "mcp_uptime_kuma_open.tools.get_specific_monitor",
        return_value=mock_data
    )
    tools.register_tools(mcp)
    get_specific_monitor_tool = await mcp.get_tool("get_specific_uptime_kuma_monitor")
    monitor_id = 2

    # ACT
    result = await get_specific_monitor_tool.run(arguments={"id": monitor_id})

    # ASSERT
    mock_get_specific_monitor.assert_called_once_with(monitor_id)
    assert json.loads(result.content[0].text) == mock_data

@pytest.mark.asyncio
async def test_get_specific_uptime_kuma_monitor_not_found(mocker):
    """
    GIVEN a FastMCP instance and a mocked service layer that raises an error
    WHEN the get_specific_uptime_kuma_monitor tool is called with a non-existent ID
    THEN it should raise a ToolError
    """
    # ARRANGE
    mcp = FastMCP()
    mocker.patch(
        "mcp_uptime_kuma_open.tools.get_specific_monitor",
        side_effect=ToolError("Monitor not found")
    )
    tools.register_tools(mcp)
    get_specific_monitor_tool = await mcp.get_tool("get_specific_uptime_kuma_monitor")
    monitor_id = 999

    # ACT & ASSERT
    with pytest.raises(ToolError, match="Monitor not found"):
        await get_specific_monitor_tool.run(arguments={"id": monitor_id})

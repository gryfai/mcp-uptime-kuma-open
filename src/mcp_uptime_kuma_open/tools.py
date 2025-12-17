from fastmcp import FastMCP
from services import (
    get_all_monitors,
    get_specific_monitor
)


def register_tools(free_mcp: FastMCP):

    @free_mcp.tool()
    async def get_uptime_kuma_monitors() -> list[dict]:
        """
        Tool is used to get all available monitors for Uptime Kuma. As soon as
        a call is made to handle all monitors, this method will return a list with
        all the monitors available. When a user requests to see all monitors this
        is the tool to use.
        :return: A list of dictionaries containing all monitors available.
        """
        return get_all_monitors()

    @free_mcp.tool()
    async def get_specific_uptime_kuma_monitor(id: int) -> dict:
        """
        This tool is used to get a specific Uptime Kuma monitor if the user
        specify a monitor id as an integer. This tool does NOT find a monitor
        if not an integer is a part of the query.
        :param id: An integer that targets a specific monitor
        :return: A dictionary with the specific Uptime Kuma Monitor
        """
        return get_specific_monitor(id)
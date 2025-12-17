from fastmcp import FastMCP
from services import (
    get_all_monitors,
    get_specific_monitor,
    get_specific_monitor_beats,
    get_all_heartbeats
)


def register_tools(free_mcp: FastMCP):

    @free_mcp.tool()
    def get_uptime_kuma_monitors() -> list[dict]:
        """
        Tool is used to get all available monitors for Uptime Kuma. As soon as
        a call is made to handle all monitors, this method will return a list with
        all the monitors available. When a user requests to see all monitors this
        is the tool to use.
        :return: A list of dictionaries containing all monitors available.
        """
        return get_all_monitors()

    @free_mcp.tool()
    def get_specific_uptime_kuma_monitor(id: int) -> dict:
        """
        This tool is used to get a specific Uptime Kuma monitor if the user
        specify a monitor id as an integer. This tool does NOT find a monitor
        if not an integer is a part of the query.
        :param id: An integer that targets a specific monitor
        :return: A dictionary with the specific Uptime Kuma Monitor
        """
        return get_specific_monitor(id)

    @free_mcp.tool()
    def get_all_monitor_heartbeats() -> dict:
        """
        Gets all heartbeats per monitor. The first integer in the response is
        the monitor id, followed by a list of its heartbeats. This tool is used
        to get all monitor heartbeats from all monitors. It can be used to get
        and further filter or do other operations per monitor - non-destructive such!

        :return: Dictionary with all beats per monitor.
        """
        return get_all_heartbeats()



    @free_mcp.tool()
    def get_monitor_beats_per_id(
            id: int,
            hours: int
    ) -> list[dict]:
        """
        This tool is used to get monitor beats per monitor id. Monitor id is defined
        via an Id and is required to get the beat. It also takes in an "hours" as an integer
        to specify the time frame in hours from now to the hours:int.

        :param id: Monitor id.
        :param hours: Hours from now. Counting backwards.
        :return: Dictionary with Beats
        """
        return get_specific_monitor_beats(id, hours)
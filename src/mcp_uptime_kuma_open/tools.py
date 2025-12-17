from fastmcp import FastMCP
from services import (
    get_all_monitors,
    get_specific_monitor,
    get_specific_monitor_beats,
    get_all_heartbeats,
    get_all_proxies as get_all_proxies_service,
    get_specific_proxy,
    get_all_status_pages,
    get_specific_status_page,
    get_all_notifications,
    get_specific_notification,
    get_average_ping,
    get_server_info,
    get_general_uptime,
    get_all_tags,
    get_specific_tag,
    get_current_settings,
    get_all_maintenances,
    get_down_monitors_service,
    get_monitor_health_summary_service,
    get_monitors_by_tag_service
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

    @free_mcp.tool()
    def get_all_proxies() -> list[dict]:
        """
        This tool returns all Uptime Kuma registered proxies. When a user asks to see
        all the proxies available, this is the tool to use. This can also be used if the user
        wants to read all but also want to filter or do operations on proxies - non-destructive ones!
        :return:
        """
        return get_all_proxies_service()

    @free_mcp.tool()
    def get_specific_proxy_by_id(id: int) -> dict:
        """
        Gets a specific proxy if a proxy id as integer is provided. This tool is used
        when a user wants to inspect a single proxy and shares the integer id.
        :param id: Proxy id
        :return: Proxy as dictionary
        """
        return get_specific_proxy(id)

    @free_mcp.tool()
    def get_all_available_status_pages() -> list[dict]:
        """
        Gets all available status pages from Uptime Kuma. This tool is used when a user
        asks to see all status pages. It can also be used to fetch all status pages and then do
        operations or filtration - non-destructive ones.
        :return: All available status pages as a list of dictionaries
        """
        return get_all_status_pages()

    @free_mcp.tool()
    def get_specific_status_page_per_slug(slug: str) -> dict:
        """
        Gets a specific status page per provided slug. If a user wants to see a specific status page
        and specifieds the required slug then this is the tool to use for that.
        :param slug: String that acts like an id
        :return: A Status page as a dictionary
        """
        return get_specific_status_page(slug)

    @free_mcp.tool()
    def get_all_uptime_kuma_notifications() -> list[dict]:
        """
        Gets all notifications from Uptime Kuma. When the user asks to review or list all
        notifications, this tool is used to return everything available.
        :return: List of notifications as dictionaries
        """
        return get_all_notifications()

    @free_mcp.tool()
    def get_specific_uptime_kuma_notification(id: int) -> dict:
        """
        Gets a specific notification if a notification id is provided as an integer.
        This tool is used when the user asks for a particular notification and provides the id.
        :param id: Notification id
        :return: Notification as dictionary
        """
        return get_specific_notification(id)

    @free_mcp.tool()
    def get_average_ping_from_uptime_kuma() -> dict:
        """
        Gets the average ping returned by Uptime Kuma. When a user wants to see the average ping
        across monitors, this tool is used.
        :return: Average ping as dictionary
        """
        return get_average_ping()

    @free_mcp.tool()
    def get_uptime_kuma_info() -> dict:
        """
        Gets general information from the Uptime Kuma server instance.
        :return: Information as dictionary
        """
        return get_server_info()

    @free_mcp.tool()
    def get_general_uptime_information() -> dict:
        """
        Gets overall uptime information from Uptime Kuma.
        :return: Uptime information as dictionary
        """
        return get_general_uptime()

    @free_mcp.tool()
    def get_all_uptime_kuma_tags() -> list[dict]:
        """
        Gets all tags available in Uptime Kuma. When a user asks for all tags this tool should be used.
        :return: List of tags as dictionaries
        """
        return get_all_tags()

    @free_mcp.tool()
    def get_specific_tag_by_id(id: int) -> dict:
        """
        Gets a specific tag if an id is provided. Use this tool when a user shares a tag id
        to retrieve its full details.
        :param id: Tag id as integer
        :return: Tag as dictionary
        """
        return get_specific_tag(id)

    @free_mcp.tool()
    def get_uptime_kuma_settings() -> dict:
        """
        Gets the current Uptime Kuma settings.
        :return: Settings as dictionary
        """
        return get_current_settings()

    @free_mcp.tool()
    def get_all_uptime_kuma_maintenances() -> list[dict]:
        """
        Gets all maintenance windows configured in Uptime Kuma. Use when a user wants to
        review every maintenance slot.
        :return: List of maintenances as dictionaries
        """
        return get_all_maintenances()


    @free_mcp.tool()
    def get_down_monitors() -> list[dict]:
        """
        Gets a list of all monitors that are currently in a 'down' state.
        Provides a quick way to check for immediate problems.
        :return: A list of monitor dictionaries that are currently down.
        """
        return get_down_monitors_service()

    @free_mcp.tool()
    def get_monitor_health_summary(id: int) -> dict:
        """
        Gets a combined health summary for a specific monitor, including
        details, average ping, and uptime information.
        :param id: The integer ID of the monitor.
        :return: A dictionary containing the combined health summary.
        """
        return get_monitor_health_summary_service(id)

    @free_mcp.tool()
    def get_monitors_by_tag(tag: str) -> list[dict]:
        """
        Finds all monitors associated with a specific tag by searching
        both tag names and tag values.
        :param tag: The tag name or value to search for (case-insensitive).
        :return: A list of monitor dictionaries that have the specified tag.
        """
        return get_monitors_by_tag_service(tag)

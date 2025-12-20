from uk_client import KumaService
from os import getenv
from dotenv import load_dotenv
from fastmcp.exceptions import ToolError

load_dotenv()

UPTIME_KUMA_URL = getenv("UPTIME_KUMA_URL", "http://localhost:3001")
UPTIME_KUMA_USERNAME = getenv("UPTIME_KUMA_USERNAME", None)
UPTIME_KUMA_PASSWORD = getenv("UPTIME_KUMA_PASSWORD", None)

if not UPTIME_KUMA_USERNAME or not UPTIME_KUMA_PASSWORD:
    raise ValueError(
        "UPTIME_KUMA_USERNAME and UPTIME_KUMA_PASSWORD must be set in your environment."
    )

kuma_service = KumaService(
    UPTIME_KUMA_URL, UPTIME_KUMA_USERNAME, UPTIME_KUMA_PASSWORD
)

def get_all_monitors() -> list[dict]:
    """
    Gets a list of Uptime Kuma Monitors.
    :return: List of Uptime Kuma Monitors
    """
    try:
        with kuma_service as api:
            return api.get_monitors()
    except Exception as e:
        raise ToolError(e)

def get_specific_monitor(id_: int) -> dict:
    """
    Gets a specific Uptime Kuma Monitor by Id. Id needs to be integer.
    Use the Id (integer) to interact with a specific monitor. Whenever the user
    asks for a special monitor and provides an integer as an Id, this is the method that is used.
    :param id_: Integer Id of monitor
    :return: dictionary of monitor
    """
    try:
        with kuma_service as api:
            return api.get_monitor(id_)
    except Exception as e:
        raise ToolError(e)

def get_specific_monitor_beats(
        id_: int, hours: int
) -> list[dict]:
    """
    Gets a specific monitor beat per ID specified as an integer.
    :param id_: Integer ID of the monitor
    :param hours: Time period from now
    :return: Monitor beats as list of dictionaries.
    """
    try:
        with kuma_service as api:
            return api.get_monitor_beats(id_, hours)
    except Exception as e:
        raise ToolError(e)


def get_all_heartbeats() -> dict:
    """
    Gets all heartbeats available for all monitors.
    :return: Dictionary with all heartbeats
    """
    try:
        with kuma_service as api:
            return api.get_heartbeats()
    except Exception as e:
        raise ToolError(e)


def get_all_notifications() -> list[dict]:
    """
    :return: List with all notifications as dictionaries
    """
    try:
        with kuma_service as api:
            return api.get_notifications()
    except Exception as e:
        raise ToolError(e)

def get_specific_notification(id: int) -> dict:
    """
    Gets a specific notification from Uptime Kuma
    :param id: Notification id
    :return: Notification as dictionary
    """
    try:
        with kuma_service as api:
            return api.get_notification(id)
    except Exception as e:
        raise ToolError(e)

def get_all_proxies() -> list[dict]:
    """
    Get all proxies from Uptime Kuma
    :return: All proxies as lists of dictionaries
    """
    try:
        with kuma_service as api:
            return api.get_proxies()
    except Exception as e:
        raise ToolError(e)


def get_specific_proxy(id: int) -> dict:
    """
    Gets specific proxy per proxy id (integer).
    :param id: Proxy Id as integer
    :return: Proxy as dictionary
    """
    try:
        with kuma_service as api:
            return api.get_proxy(id)
    except Exception as e:
        raise ToolError(e)

def get_all_status_pages() -> list[dict]:
    """
    Gets all status pages for consumption.
    :return: All status pages as list of dictionaries
    """
    try:
        with kuma_service as api:
            return api.get_status_pages()
    except Exception as e:
        raise ToolError(e)


def get_specific_status_page(slug: str) -> dict:
    """
    Gets a specific status page from Uptime Kuma
    :param slug: Identifier string of the status page
    :return: Status page as dictionary
    """
    try:
        with kuma_service as api:
            return api.get_status_page(slug)
    except Exception as e:
        raise ToolError(e)


def get_average_ping() -> dict:
    """
    Gets the average ping per Uptime Kuma.
    :return: Average ping as a dictionary
    """
    try:
        with kuma_service as api:
            return api.avg_ping()
    except Exception as e:
        raise ToolError(e)


def get_server_info() -> dict:
    """
    Gets general server information from Uptime Kuma.
    :return: Dictionary with server info
    """
    try:
        with kuma_service as api:
            return api.info()
    except Exception as e:
        raise ToolError(e)


def get_general_uptime() -> dict:
    """
    Gets Uptime Kuma uptime.
    :return: Dictionary with uptime information
    """
    try:
        with kuma_service as api:
            return api.uptime()
    except Exception as e:
        raise ToolError(e)


def get_all_tags() -> list[dict]:
    """
    Gets all tags registered in Uptime Kuma.
    :return: List of tags as dictionaries
    """
    try:
        with kuma_service as api:
            return api.get_tags()
    except Exception as e:
        raise ToolError(e)


def get_specific_tag(id_: int) -> dict:
    """
    Gets a specific tag per tag id.
    :param id_: Tag id as integer
    :return: Tag as dictionary
    """
    try:
        with kuma_service as api:
            return api.get_tag(id_)
    except Exception as e:
        raise ToolError(e)


def get_current_settings() -> dict:
    """
    Gets current Uptime Kuma settings.
    :return: Settings as dictionary
    """
    try:
        with kuma_service as api:
            return api.get_settings()
    except Exception as e:
        raise ToolError(e)


def get_all_maintenances() -> list[dict]:
    """
    Gets all maintenance windows.
    :return: List of maintenances as dictionaries
    """
    try:
        with kuma_service as api:
            return api.get_maintenances()
    except Exception as e:
        raise ToolError(e)


def get_down_monitors_service() -> list[dict]:
    """
    Gets a list of all monitors that are currently down.
    :return: A list of monitor dictionaries.
    """
    try:
        with kuma_service as api:
            all_monitors = api.get_monitors()
            # Status 0 is down
            down_monitors = [
                monitor for monitor in all_monitors if monitor.get("status") == 0
            ]
            return down_monitors
    except Exception as e:
        raise ToolError(e)


def get_monitor_health_summary_service(id_: int) -> dict:
    """
    Gets a combined health summary for a specific monitor.
    :param id_: The ID of the monitor.
    :return: A dictionary containing combined health information.
    """
    try:
        with kuma_service as api:
            monitor_details = api.get_monitor(id_)
            average_ping = api.avg_ping().get(str(id_))
            uptime_info = api.uptime().get(str(id_))

            summary = {
                "details": monitor_details,
                "average_ping": average_ping,
                "uptime": uptime_info,
            }
            return summary
    except Exception as e:
        raise ToolError(e)


def get_monitors_by_tag_service(tag: str) -> list[dict]:
    """
    Finds all monitors associated with a specific tag.
    :param tag: The tag name or value to search for.
    :return: A list of monitor dictionaries that have the specified tag.
    """
    try:
        with kuma_service as api:
            all_monitors = api.get_monitors()
            tagged_monitors = []
            for monitor in all_monitors:
                for monitor_tag in monitor.get("tags", []):
                    # Check if the search tag is in the tag's name or value
                    if tag.lower() in monitor_tag.get("name", "").lower() or \
                       tag.lower() in monitor_tag.get("value", "").lower():
                        tagged_monitors.append(monitor)
                        break  # Move to the next monitor once a match is found
            return tagged_monitors
    except Exception as e:
        raise ToolError(e)


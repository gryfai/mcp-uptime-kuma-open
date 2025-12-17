from uk_client import KumaService
from os import getenv
from dotenv import load_dotenv
from fastmcp.exceptions import ToolError

load_dotenv()

UPTIME_KUMA_URL=getenv("UPTIME_KUMA_URL", "http://localhost:3001")
UPTIME_KUMA_USERNAME=getenv("UPTIME_KUMA_USERNAME", None)
UPTIME_KUMA_PASSWORD=getenv("UPTIME_KUMA_PASSWORD", None)

kuma_service = KumaService(UPTIME_KUMA_URL,UPTIME_KUMA_USERNAME, UPTIME_KUMA_PASSWORD)

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
            return api.get_monitor_beats(id, hours)
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
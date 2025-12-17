from uk_client import KumaService
from os import getenv
from dotenv import load_dotenv

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
    with kuma_service as api:
        return api.get_monitors()


def get_specific_monitor(id_: int) -> dict:
    """
    Gets a specific Uptime Kuma Monitor by Id. Id needs to be integer.
    Use the Id (integer) to interact with a specific monitor. Whenever the user
    asks for a special monitor and provides an integer as an Id, this is the method that is used.
    :param id_: Integer Id of monitor
    :return: dictionary of monitor
    """
    with kuma_service as api:
        return api.get_monitor(id_)


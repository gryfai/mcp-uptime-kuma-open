from uk_client import KumaService


def get_monitors(kuma_service: KumaService) -> list[dict]:
    """
    Gets a list of Uptime Kuma Monitors.

    :param kuma_service:
    :return: List of Uptime Kuma Monitors
    """
    with kuma_service as api:
        return api.get_monitors()


def get_monitor(id_: int, kuma_service: KumaService) -> dict:
    """
    Gets a specific Uptime Kuma Monitor by Id. Id needs to be integer.
    :param id_: Id of monitor
    :param kuma_service:
    :return: dictionary of monitor
    """
    with kuma_service() as api:
        return api.get_monitor(id_)


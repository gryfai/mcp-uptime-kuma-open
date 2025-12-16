from fastmcp import FastMCP
from services import (
    get_monitors
)


UPTIME_KUMA_URL=getenv("UPTIME_KUMA_URL", "http://localhost:3001")
UPTIME_KUMA_USERNAME=getenv("UPTIME_KUMA_USERNAME", None)
UPTIME_KUMA_PASSWORD=getenv("UPTIME_KUMA_PASSWORD", None)

serv = KumaService(UPTIME_KUMA_URL,UPTIME_KUMA_USERNAME,UPTIME_KUMA_PASSWORD)


free_mcp = FastMCP("Free Uptime Kuma MCP server")

@free_mcp.tool()
async def get_monitors() -> list[dict]:
    """
    Tool is used to get all available monitors for Uptime Kuma. As soon as
    a call is made to handle all monitors, this method will return a list with
    all the monitors available.
    :return: A list of dictionaries containing all monitors available.
    """
    return get_monitors(serv)
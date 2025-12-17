from fastmcp import FastMCP
from tools import register_tools

free_mcp = FastMCP("Free Uptime Kuma MCP server")

register_tools(free_mcp)

if __name__ == '__main__':
    free_mcp.run()
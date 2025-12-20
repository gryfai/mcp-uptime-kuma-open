from fastmcp import FastMCP
from .tools import register_tools

def main():
    free_mcp = FastMCP("Free Uptime Kuma MCP server")
    register_tools(free_mcp)
    free_mcp.run()

if __name__ == '__main__':
    main()
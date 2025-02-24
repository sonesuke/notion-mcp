import asyncio
import mcp.types as types
from mcp.server import Server
from mcp.server.stdio import stdio_server

app = Server("example-server")


@app.list_resources()  # type: ignore
async def list_resources() -> list[types.Resource]:
    return [types.Resource(uri="example://resource", name="Example Resource")]


# pragma: no cover
async def main() -> None:
    async with stdio_server() as streams:
        await app.run(streams[0], streams[1], app.create_initialization_options())


# pragma: no cover
def run_main() -> None:
    asyncio.run(main())


if __name__ == "__main__":
    run_main()

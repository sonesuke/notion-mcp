import mcp.types as types
from mcp.server import Server
from notion_client import Client
import os


app = Server("Notion server")


@app.list_tools()  # type: ignore
async def list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="create_page",
            description="Create new Notion page",
            inputSchema={
                "type": "object",
                "properties": {
                    "title": {"type": "string", "description": "Title of the page"},
                    "contents": {
                        "type": "string",
                        "description": "Contents of the page",
                    },
                },
                "required": ["title", "contents"],
            },
        )
    ]


@app.call_tool()  # type: ignore
async def create_page(
    name: str, arguments: dict[str, str]
) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """
    Create a new page in Notion with the given title and contents.
    Args:
        name : The name of the tool, must be "create_page".
        arguments : A dictionary containing the title and contents of the page.
            - "title": The title of the new page.
            - "contents": The contents of the new page.
    Returns:
        A list containing a success message as TextContent.
    Raises:
        ValueError: If the name is not "create_page".
    """

    if name != "create_page":
        raise ValueError(f"Tool not found: {name}")

    parent_page_id = os.environ["PARENT_PAGE_ID"]
    notion = Client(auth=os.environ["NOTION_API_KEY"])

    title = arguments["title"]
    contents = arguments["contents"]

    notion.pages.create(
        parent={"page_id": parent_page_id},
        properties={
            "type": "title",
            "title": [{"type": "text", "text": {"content": title}}],
        },
        children=[
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {"content": contents},
                        }
                    ]
                },
            }
        ],
    )
    return [types.TextContent(type="text", text="Notion page created successfully")]

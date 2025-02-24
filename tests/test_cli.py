import pytest
from notion_mcp.core import list_tools, create_page
from pytest_mock import MockerFixture
import os
import notion_client


@pytest.mark.asyncio  # type: ignore
async def test_list_tools() -> None:
    result = await list_tools()
    assert len(result) == 1
    assert result[0].name == "create_page"
    assert result[0].description == "Create new Notion page"
    assert result[0].inputSchema == {
        "type": "object",
        "properties": {
            "title": {"type": "string", "description": "Title of the page"},
            "contents": {"type": "string", "description": "Contents of the page"},
        },
        "required": ["title", "contents"],
    }


@pytest.mark.asyncio  # type: ignore
async def test_create_page(mocker: MockerFixture) -> None:
    patch = mocker.patch("notion_client.Client.request")
    os.environ["PARENT_PAGE_ID"] = "dummy page id"
    os.environ["NOTION_API_KEY"] = "dummy notion api key"

    result = await create_page("create_page", {"title": "test", "contents": "test"})

    notion_client.Client.request.assert_called_once()
    _, kwargs = patch.call_args
    assert kwargs["path"] == "pages"
    assert kwargs["method"] == "POST"
    assert kwargs["body"] == {
        "parent": {"page_id": "dummy page id"},
        "properties": {
            "type": "title",
            "title": [{"type": "text", "text": {"content": "test"}}],
        },
        "children": [
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {"content": "test"},
                        }
                    ]
                },
            }
        ],
    }
    assert result[0].text == "Notion page created successfully"


@pytest.mark.asyncio  # type: ignore
async def test_call_tool_invalid_tool() -> None:
    with pytest.raises(ValueError, match="Tool not found: invalid_tool"):
        await create_page("invalid_tool", {})

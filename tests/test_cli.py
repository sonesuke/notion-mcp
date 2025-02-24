import pytest
from notion_mcp.cli import list_resources


@pytest.mark.asyncio  # type: ignore
async def test_list_resources() -> None:
    result = await list_resources()
    assert len(result) == 1

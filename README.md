# Notion MCP

This project is a sample implementation of MCP for creating Notion pages.

## Features

- Create new Notion pages from markdown files

## How to Use with Goose

To integrate this project with Goose, follow these steps:

1. Install the MCP server on Goose:
    ```sh
    goose configure
    ```

2. Add the extension to your project with a preferred name:
    ```sh
    Add Extension (Connect to a new extension)
    Command-line Extension (Run a local command or script)
    ```

3. Configure the settings:

    - Command: `uvx --from git+https://github.com/sonesuke/notion-mcp@main cli`
    - Environment Variables:
        - `PARENT_PAGE_ID`: Your parent page ID
        - `NOTION_API_KEY`: Your API key

4. Start a Goose session:
    ```sh
    goose session
    ```

5. Execute the command through the extension:
    ```sh
    Create a Notion page about Kyoto
    ```

## Prerequisites for Development

Ensure you have the following installed:

- Python 3.6+
- uv
- pre-commit
- just

# Development


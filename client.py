# Import required libraries
import asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client

async def run():
    # Connect to MCP server over stdio or sse
    async with sse_client("http://localhost:8000/sse") as streams:
        async with ClientSession(*streams) as session:

            # Initialize the session
            await session.initialize()

            # List available tools
            tools = await session.list_tools()
            print(tools)
            # We can integrate these tools with our LLM application too


            # Call the summarize_text tool
            result = await session.call_tool("summarize_text", {
                "text": "MCP is an open protocol that standardizes how applications provide context to LLMs. Think of MCP like a USB-C port for AI applications. Model Context Protocol enables seamless tool and resource integration for language models."
            })
            print("📝 Summary:", result.content[0].text)

            # Call the cat_fact tool
            result = await session.call_tool("cat_fact")
            print("📖 Cat Fact:", result.content[0].text)

            # Call the execute_code tool
            result = await session.call_tool("execute_code", {
                "code": "result = 42 * 2"
            })
            print("💻 Code Execution Result:", result.content[0].text)

if __name__ == "__main__":
    asyncio.run(run())

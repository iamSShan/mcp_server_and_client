from mcp.server.fastmcp import FastMCP # is a Python framework designed to simplify the creation of MCP servers
import requests
from transformers import pipeline

# Initialize the MCP server
mcp = FastMCP('Demo Server')

# Create tools:


# 1. Summarization Agent
# We can use open AI chat gpt as summarization tool like this:
# @mcp.tool()
# async def summarize_text(text: str) -> str:
#     """Summarizes the provided text."""
#     openai.api_key = 'your-openai-api-key'
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=f"Summarize the following text:\n\n{text}",
#         max_tokens=150
#     )
#     return response.choices[0].text.strip()

# But let's use an offline version for now

# Load summarization pipeline (this will download the model the first time)
summarizer = pipeline("summarization", model="t5-small", tokenizer="t5-small")

@mcp.tool()
async def summarize_text(text: str) -> str:
    """Summarizes the given text using Hugging Face BART model."""
    summary = summarizer(text, max_length=40, min_length=10, do_sample=False)
    return summary[0]['summary_text']

# Random Cat Fact Agent
@mcp.tool()
async def cat_fact() -> str:
    """Returns a random cat fact."""
    return requests.get("https://catfact.ninja/fact").json()["fact"]

# Code Execution Agent
@mcp.tool()
async def execute_code(code: str) -> str:
    """Executes a Python code snippet."""
    try:
        exec_globals = {}
        exec(code, exec_globals)
        return str(exec_globals.get("result", "No result variable defined"))
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    # Initialize and run server
    mcp.run(transport='sse') # stdio is for local, sse can be used in cloud
    # We can still use sse in local, read more here: https://modelcontextprotocol.io/docs/concepts/transports

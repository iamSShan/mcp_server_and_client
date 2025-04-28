# MCP Server and Client

This project provides a minimal working example of the Model Context Protocol (MCP), demonstrating how to set up a FastMCP server with basic tools and interact with it using an MCP client. It serves as a simple reference for understanding how MCP-based communication between agents and tools can be implemented.


---

## Setup Instructions

### 1. Install `uv`

```bash
	python -m pip install uv
```


### 2. Initialize the Project and activate the env

```bash
	uv init mcp_server_for_llm_agents

	uv venv

	source .venv/bin/activate
```



### 3. Install dependencies

```bash
uv pip install -r requirements.txt
```
---

## Server
Your agent tools (e.g., summarize_text, code executin, etc.) should be implemented in server.py
Run the server with:

```bash
	uv run mcp dev server.py
```

Or directly:

```bash
	python server.py
```


## Client

A client using the official MCP SDK is defined in client.py

Run using:
```bash
	python client.py
```

It connects to the MCP server and calls tools like: `summarize_text`, `cat_fact`, `execute_code present` in server.py 


After running we can see results in terminal for now

---

## References:
* [MCP Server Quickstart](https://modelcontextprotocol.io/quickstart/server)
* [MCP Client Quickstart](https://modelcontextprotocol.io/quickstart/client)
* [MCP Python SDK GitHub](https://github.com/modelcontextprotocol/python-sdk)
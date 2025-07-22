# GenAI template 🚀

A template for your kickstart into GenAI! 🎁

It combines [Docker Model Runner](https://docs.docker.com/ai/model-runner/), [LangChain/LangGraph](https://www.langchain.com/), [marimo](https://github.com/marimo-team/marimo), [Open WebUI](https://openwebui.com/), [Agent Chat UI](https://github.com/langchain-ai/agent-chat-ui) and [Agent Inbox](https://github.com/langchain-ai/agent-inbox)!

## How to use

To spin up all services run:

`make run`

This will spin up the following services:

- [`localhost:8000`](http://localhost:8000): [marimo](https://github.com/marimo-team/marimo)
- [`localhost:8080`](http://localhost:8080): [Open WebUI](https://openwebui.com/)
- [`localhost:2024`](http://localhost:2024): [LangGraph Server API](https://langchain-ai.github.io/langgraph/)
- [`localhost:3000`](http://localhost:5173): [Agent Chat UI](https://github.com/langchain-ai/agent-chat-ui)
- [`localhost:3000`](http://localhost:3000): [Agent Inbox](https://github.com/langchain-ai/agent-inbox)
- [`localhost:6274`](http://localhost:6274): [MCP Inspector](https://github.com/modelcontextprotocol/inspector)

## Components

### Jupyter

If you work with Jupyter, you can use the `jupyter` folder to store your notebooks and other files.
You can add your requirements to the `jupyter/requirements.txt` file, and they will be installed in the Jupyter container.

### LangGraph Server

You can define your LangGraph graph in the `langgraph_server` folder. The requirements are automatically installed from the `langgraph_server/requirements.txt` file.

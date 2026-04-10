import marimo

__generated_with = "0.23.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Agent example
    """)
    return


@app.cell
def _():
    import os
    from langchain_openai import ChatOpenAI

    llm_url = os.environ.get("QWEN3_URL")
    llm_model = os.environ["QWEN3_MODEL"]
    llm = ChatOpenAI(base_url=llm_url, model=llm_model, openai_api_key="docker")
    return (llm,)


@app.cell
def _():
    from langchain_core.tools import tool


    @tool
    def get_weather(city: str) -> str:
        """Get the current weather for a specified city.

        Args:
            city: The name of the city.
        """
        print("using weather tool")
        return f"The weather in {city} is sunny and 22 degrees Celsius."


    @tool
    def calculate_sum(a: int, b: int) -> int:
        """Add two numbers together.

        Args:
            a: First integer.
            b: Second integer.
        """
        print(f"Using calculate_sum tool: {a} + {b}")
        return a + b


    tools = [get_weather, calculate_sum]
    return (tools,)


@app.cell
def _(llm, tools):
    from langchain.agents import create_agent

    agent = create_agent(
        model=llm,
        tools=tools,
    )

    if __name__ == "__main__":
        print("Agent is thinking...\n")
        response = agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": "What is 4792749 plus 5798374 plus 478379345?",
                    }
                ]
            }
        )
        print(response["messages"][-1].content)
    return


if __name__ == "__main__":
    app.run()

import marimo

__generated_with = "0.14.12"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# LLM examples""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Option 1: Docker model runner (locally running models)""")
    return


@app.cell
def _():
    import os
    from langchain_openai import ChatOpenAI

    llm_url = os.environ.get("SMOLLM2_URL")
    llm_model = os.environ.get("SMOLLM2")
    llm = ChatOpenAI(base_url=llm_url, model=llm_model, openai_api_key="docker")

    llm.invoke("What does the fox say?")
    return


if __name__ == "__main__":
    app.run()

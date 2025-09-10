import marimo

__generated_with = "0.15.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import os
    from typing import Optional

    import requests

    Embedding = list[float]

    task_prompt_prefixes = {
        "query": "task: search result | query: ",
        "document": "title: none | text: ",
        "BitextMining": "task: search result | query: ",
        "Clustering": "task: clustering | query: ",
        "Classification": "task: classification | query: ",
        "InstructionRetrieval": "task: code retrieval | query: ",
        "MultilabelClassification": "task: classification | query: ",
        "PairClassification": "task: sentence similarity | query: ",
        "Reranking": "task: search result | query: ",
        "Retrieval": "task: search result | query: ",
        "Retrieval-query": "task: search result | query: ",
        "Retrieval-document": "title: none | text: ",
        "STS": "task: sentence similarity | query: ",
        "Summarization": "task: summarization | query: ",
    }


    def get_text_embedding(
        text: str, task_name: Optional[str] = None
    ) -> Embedding:
        task_prefix = task_prompt_prefixes.get(task_name)

        url = f"{os.environ['EMBEDDINGGEMMA_URL']}embeddings"
        headers = {"Content-Type": "application/json"}
        data = {
            "input": f"{task_prefix}{text}",
            "model": os.environ["EMBEDDINGGEMMA_MODEL"],
        }

        raw_response = requests.post(url, headers=headers, json=data)
        response = raw_response.json()
        return response["data"][0]["embedding"]
    return Embedding, get_text_embedding


@app.cell
def _(Embedding):
    import numpy as np
    from sklearn.metrics.pairwise import cosine_similarity


    def get_cosine_similarity(vector1: Embedding, vector2: Embedding) -> float:
        return cosine_similarity(
            np.array(vector1).reshape(1, -1), np.array(vector2).reshape(1, -1)
        )[0][0]
    return (get_cosine_similarity,)


@app.cell
def _(get_cosine_similarity, get_text_embedding):
    texts = [
        "The new smartphone model was released last week.",
        "Last week, a new mobile device was launched.",
        "The weather today is sunny with a chance of rain.",
    ]
    vectors = [get_text_embedding(text, "STS") for text in texts]

    print(get_cosine_similarity(vectors[0], vectors[1]))
    print(get_cosine_similarity(vectors[0], vectors[2]))
    print(get_cosine_similarity(vectors[1], vectors[2]))
    return


if __name__ == "__main__":
    app.run()

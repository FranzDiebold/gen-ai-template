import marimo

__generated_with = "0.14.12"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return


@app.cell
def _():
    import requests
    import json
    import os

    Embedding = list[float]


    def get_embedding(text: str) -> Embedding:
        url = f"{os.environ['EMBEDDINGGEMMA_URL']}embeddings"
        headers = {"Content-Type": "application/json"}
        data = {
            "input": text,
            "model": os.environ["EMBEDDINGGEMMA_MODEL"],
        }

        raw_response = requests.post(url, headers=headers, json=data)
        response = raw_response.json()
        return response["data"][0]["embedding"]
    return Embedding, get_embedding


@app.cell
def _(Embedding):
    import numpy as np
    from sklearn.metrics.pairwise import (
        cosine_similarity as sklearn_cosine_similarity,
    )


    def cosine_similarity(vector1: Embedding, vector2: Embedding) -> float:
        return sklearn_cosine_similarity(
            np.array(vector1).reshape(1, -1), np.array(vector2).reshape(1, -1)
        )[0][0]
    return (cosine_similarity,)


@app.cell
def _(cosine_similarity, get_embedding):
    texts = [
        "The new smartphone model was released last week.",
        "Last week, a new mobile device was launched.",
        "The weather today is sunny with a chance of rain.",
    ]
    vectors = [get_embedding(text) for text in texts]

    print(cosine_similarity(vectors[0], vectors[1]))
    print(cosine_similarity(vectors[0], vectors[2]))
    print(cosine_similarity(vectors[1], vectors[2]))
    return


if __name__ == "__main__":
    app.run()

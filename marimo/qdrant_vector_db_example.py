import marimo

__generated_with = "0.15.2"
app = marimo.App(width="medium")


@app.cell
def _():
    COLLECTION_NAME = "my_collection"
    return (COLLECTION_NAME,)


@app.cell
def _():
    import os

    import requests

    Embedding = list[float]


    def get_text_embedding(text: str) -> Embedding:
        url = f"{os.environ['EMBEDDINGGEMMA_URL']}embeddings"
        headers = {"Content-Type": "application/json"}
        data = {
            "input": text,
            "model": os.environ["EMBEDDINGGEMMA_MODEL"],
        }

        raw_response = requests.post(url, headers=headers, json=data)
        response = raw_response.json()
        return response["data"][0]["embedding"]
    return (get_text_embedding,)


@app.cell
def _():
    from qdrant_client import QdrantClient

    client = QdrantClient(host="qdrant", grpc_port=6334, prefer_grpc=True)
    return (client,)


@app.cell
def _(COLLECTION_NAME, client):
    from qdrant_client.models import Distance, VectorParams

    if not client.collection_exists(COLLECTION_NAME):
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=768, distance=Distance.COSINE),
        )
    return


@app.cell
def _():
    import hashlib
    import uuid


    def create_uuid_from_string(text: str) -> str:
        hex_string = hashlib.md5(text.encode("UTF-8")).hexdigest()
        return str(uuid.UUID(hex=hex_string))
    return (create_uuid_from_string,)


@app.cell
def _(COLLECTION_NAME, client, create_uuid_from_string, get_text_embedding):
    from qdrant_client.models import PointStruct


    def insert(text: str) -> None:
        client.upsert(
            collection_name=COLLECTION_NAME,
            points=[
                PointStruct(
                    id=create_uuid_from_string(text),
                    vector=get_text_embedding(text),
                    payload={"text": text},
                )
            ],
        )
    return (insert,)


@app.cell
def _(insert):
    texts = [
        "The new smartphone model was released last week.",
        "Last week, a new mobile device was launched.",
        "The weather today is sunny with a chance of rain.",
    ]

    for text in texts:
        insert(text)
    return


@app.cell
def _(COLLECTION_NAME, client, get_text_embedding):
    def similarity_search(text: str, limit: int = 2) -> list[str]:
        response = client.query_points(
            collection_name=COLLECTION_NAME,
            query=get_text_embedding(text),
            limit=limit,
        )
        return [point.payload["text"] for point in response.points]
    return (similarity_search,)


@app.cell
def _(similarity_search):
    print(similarity_search("iphone"))
    return


@app.cell
def _():
    import marimo as mo
    return


if __name__ == "__main__":
    app.run()

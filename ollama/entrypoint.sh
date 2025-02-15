#!/bin/bash

/bin/ollama serve &

pid=$!

sleep 5

echo "🔴 Retrieve models..."
while IFS= read -r model || [ -n "$model" ]; do
    echo "🟡 Loading model: $model"
    ollama pull "$model"
done < ./models_to_preload.txt
echo "🟢 Done!"

wait $pid
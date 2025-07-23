#!/bin/bash

npm install -g pnpm

if [ ! -d agent-chat-ui ]; then
    git clone https://github.com/langchain-ai/agent-chat-ui.git
    cd agent-chat-ui
    pnpm install
else
    cd agent-chat-ui
fi

pnpm run dev

tail -f /dev/null
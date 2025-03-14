#!/bin/bash

if [ ! -d agent-chat-ui ]; then
    npm install -g pnpm
    git clone https://github.com/langchain-ai/agent-chat-ui.git
    cd agent-chat-ui
    pnpm install
else
    cd agent-chat-ui
fi

pnpm dev --host

tail -f /dev/null
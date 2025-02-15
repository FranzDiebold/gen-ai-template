#!/bin/bash

if [ ! -d agent-inbox ]; then
    git clone https://github.com/langchain-ai/agent-inbox.git
    cd agent-inbox
    yarn install
else
    cd agent-inbox
fi

yarn dev

tail -f /dev/null
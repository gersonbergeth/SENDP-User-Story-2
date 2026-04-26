#!/bin/bash
if [ -f /usr/local/lib/workshop-devguard.sh ]; then
    source /usr/local/lib/workshop-devguard.sh
    devguard_acquire "${APP_PORT:-3000}"
fi
uv run uvicorn main:app --host 0.0.0.0 --port "${APP_PORT:-3000}"

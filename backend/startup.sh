#!/bin/bash
# Azure App Service startup script for AI Lawyer Backend (FastAPI)
# This script is used when deploying to Azure App Service (Linux).
# Set this as the startup command in the Azure Portal or via az CLI:
#   az webapp config set --startup-file startup.sh

set -e

cd /home/site/wwwroot

# Install Python dependencies if requirements.txt is present
if [ -f requirements.txt ]; then
    pip install --no-cache-dir -r requirements.txt
fi

# Export the PORT provided by Azure App Service (default: 8000)
export PORT="${PORT:-8000}"

# Start the FastAPI application with Uvicorn
exec uvicorn app.main:app \
    --host 0.0.0.0 \
    --port "$PORT" \
    --workers 2 \
    --log-level info

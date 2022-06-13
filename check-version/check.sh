#!/bin/env bash

# cron 0 3 * * * /root/minecraft-bedrock-server/check-version/check.sh

source .venv/bin/activate

NEW_VERSION=$(python main.py)

if ! [ -z "$NEW_VERSION" ]
then
    pm2 restart bedrock-server
fi
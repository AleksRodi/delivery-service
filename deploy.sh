#!/bin/bash
set -e

REPO_URL="git@github.com:AleksRodi/delivery-service.git"
PROJECT_DIR="/opt/delivery-service"
BRANCH="main"

if [ ! -d "$PROJECT_DIR" ]; then
  git clone $REPO_URL $PROJECT_DIR
fi

cd $PROJECT_DIR
git fetch
git checkout $BRANCH
git pull

docker compose down
docker compose build
docker compose up -d --remove-orphans

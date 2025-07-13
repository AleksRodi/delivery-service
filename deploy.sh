#!/bin/bash

set -e

PROJECT_DIR="/home/youruser/yourproject" # путь до проекта на ВМ
REPO_URL="https://github.com/your/repo.git"

# 1. Клонируем или обновляем проект
if [ -d "$PROJECT_DIR/.git" ]; then
  cd "$PROJECT_DIR"
  git pull
else
  git clone "$REPO_URL" "$PROJECT_DIR"
  cd "$PROJECT_DIR"
fi

# 2. Запускаем (или пересобираем) контейнеры
docker compose pull
docker compose build
docker compose up -d

echo "Деплой завершён. Backend: :8000, Frontend: :3000"

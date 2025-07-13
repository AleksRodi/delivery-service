#!/bin/bash

set -e

# Настройки
PROJECT_DIR="/root/delivery-service"          # Путь до проекта (убедитесь, что папка существует и пуста!)
REPO_URL="git@github.com:your/repo.git"       # SSH-ссылка на репозиторий
SSH_KEY="/root/.ssh/id_ed25519"               # Путь к приватному SSH-ключу

# 1. Проверяем SSH-ключ
if [ ! -f "$SSH_KEY" ]; then
  echo "❌ SSH-ключ не найден: $SSH_KEY"
  exit 1
fi

# 2. Настраиваем Git для использования SSH-ключа
export GIT_SSH_COMMAND="ssh -i $SSH_KEY -o IdentitiesOnly=yes"

# 3. Клонируем или обновляем проект
if [ -d "$PROJECT_DIR/.git" ]; then
  echo "🔄 Обновляем репозиторий..."
  cd "$PROJECT_DIR"
  git pull
else
  echo "⏬ Клонируем репозиторий..."
  rm -rf "$PROJECT_DIR" 2>/dev/null || true  # Очищаем папку, если она существует
  mkdir -p "$PROJECT_DIR"
  git clone "$REPO_URL" "$PROJECT_DIR"
  cd "$PROJECT_DIR"
fi

# 4. Запускаем Docker-контейнеры
echo "🐳 Пересобираем контейнеры..."
docker compose down || true  # Останавливаем старые контейнеры (если есть)
docker compose pull
docker compose build --no-cache  # Пересобираем без кеша (на случай проблем с зависимостями)
docker compose up -d

echo "✅ Деплой завершён. Проверьте контейнеры:"
docker ps

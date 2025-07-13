#!/bin/bash

set -e

# Настройки
PROJECT_DIR="/root/delivery-service"
REPO_URL="git@github.com:AleksRodi/delivery-service.git"
SSH_KEY="/root/.ssh/id_ed25519"

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
  
  # Сохраняем изменения в deploy.sh если они есть
  if ! git diff --quiet -- deploy.sh; then
    echo "⚠️ Обнаружены локальные изменения в deploy.sh, создаем backup..."
    cp deploy.sh deploy.sh.backup
    git checkout -- deploy.sh  # Отменяем локальные изменения
  fi
  
  git pull
  # Восстанавливаем backup если нужно
  if [ -f "deploy.sh.backup" ]; then
    echo "⚠️ Восстанавливаем backup deploy.sh..."
    mv deploy.sh.backup deploy.sh
    chmod +x deploy.sh
  fi
else
  echo "⏬ Клонируем репозиторий..."
  rm -rf "$PROJECT_DIR" 2>/dev/null || true
  mkdir -p "$PROJECT_DIR"
  git clone "$REPO_URL" "$PROJECT_DIR"
  cd "$PROJECT_DIR"
fi

# 4. Запускаем Docker-контейнеры
echo "🐳 Пересобираем контейнеры..."
docker compose down || true
docker compose pull
docker compose build --no-cache
docker compose up -d

echo "✅ Деплой завершён. Проверьте контейнеры:"
docker ps

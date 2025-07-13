# Delivery Service (FastAPI)

Микросервис для управления доставками с использованием FastAPI и PostgreSQL.

## 📌 Features
- Создание, просмотр и отмена доставок
- Асинхронное взаимодействие с БД
- Документация Swagger (доступна после запуска)

## 🚀 Quick Start

### Требования
- Docker и Docker Compose
- Python 3.9+

### Запуск
```bash
git clone https://github.com/AleksRodi/delivery-service.git
cd delivery-service

# Запуск с Docker
docker-compose up --build

# Или локально (предварительно настройте .env)
uvicorn src.main:app --reload

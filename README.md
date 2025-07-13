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

📄 API Documentation

После запуска откройте:

    Swagger UI: http://localhost:8000/docs

    Redoc: http://localhost:8000/redoc

# Создать доставку
curl -X POST "http://localhost:8000/api/v1/deliveries" \
  -H "Content-Type: application/json" \
  -d '{"order_id": 123, "address": "Moscow, Kremlin", "phone": "+79991234567"}'

🛠️ Development

    Тесты: pytest tests/

    Линтинг: flake8 src/

---

### **2. Фиксация зависимостей**
**Файл:** `requirements.txt`  
**Содержание:**
```text
fastapi==0.95.2
uvicorn==0.22.0
asyncpg==0.27.0
pydantic==1.10.7
python-dotenv==1.0.0
pytest==7.4.0
pytest-asyncio==0.21.1
flake8==6.1.0

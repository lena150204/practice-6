from fastapi import FastAPI
from routes.users import user_router
from routes.events import event_router
import uvicorn


# 1. Создаем экземпляр приложения
app = FastAPI(
    title="Event Planner API",
    description="Учебный проект — планировщик событий",
    version="1.0.0"
)

# 2. Подключаем роутеры с префиксами
# Все маршруты из user_router получат префикс /user
app.include_router(user_router, prefix="/user")

# Все маршруты из event_router получат префикс /event
app.include_router(event_router, prefix="/event")


# 3. Запуск сервера
if __name__ == "__main__":
    uvicorn.run(
        "main:app",       # путь к приложению (файл main.py, объект app)
        host="0.0.0.0",   # слушать все сетевые интерфейсы
        port=8080,        # порт
        reload=True       # автоперезагрузка при изменении кода
    )
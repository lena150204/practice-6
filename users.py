from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSignIn, NewUser


# Создаем роутер с тегом "User" (в Swagger будет отдельная секция)
user_router = APIRouter(tags=["User"])


# ⚠ ВНИМАНИЕ: это временное хранилище в памяти.
# В реальном проекте здесь будет база данных (см. database/connection.py).
users = {}


@user_router.post("/signup")
async def sign_new_user(data: NewUser) -> dict:
    """
    Регистрация нового пользователя.
    Принимает объект NewUser (email + password).
    Возвращает сообщение об успехе.
    """
    # Проверяем, что пользователь с таким email еще не зарегистрирован
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied username exists"
        )

    # Сохраняем пользователя в словарь (ключ — email)
    users[data.email] = data
    return {"message": "User successfully registered!"}


@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    """
    Вход пользователя в систему.
    Проверяет: существует ли пользователь и верный ли пароль.
    """
    # 1. Проверяем наличие пользователя
    if user.email not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )

    # 2. Проверяем пароль
    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wrong credentials passed"
        )

    return {"message": "User signed in successfully"}
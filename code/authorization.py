from config import SALT, JSON_PATH_USERS
from work_with_json import add_to_json, check_in_json
import hashlib

def password_validation(password: str) -> bool:
    if len(password) <= 8:
        raise ValueError("Длина пароля должна составлять минимум 8 символов")

    if password in [password.upper(), password.lower()]:
        raise ValueError("Пароль должен содержать хотя бы одну маленькую и хотя бы одну заглавную буквы")

    if not any(map(lambda x: x.isalpha(), list(password))):
        raise ValueError("Пароль должен содержать хотя бы одну прописную букву")

    if not any(map(lambda x: x.isdigit(), list(password))):
        raise ValueError("Пароль должен содержать хотя бы одну цифру")

    if not any(map(lambda x: x in "!@#$%^&*()_+{}\":;'", list(password))):
        raise ValueError("Пароль должен содержать хотя бы один спец. символ")

    return True


def hashing_password(password):
    return hashlib.sha256((password + SALT).encode("utf-8")).hexdigest()


def registration(login: str, password: str) -> tuple:
    try:
        password_validation(password)

    except Exception as password_error_message:
        return (False, password_error_message)

    try_add_user = add_to_json(JSON_PATH_USERS, (login, hashing_password(password)))

    if try_add_user:
        return (True, None)

    return (False, "Пользователь с таким логином уже существует")


def sign_in(login: str, password: str) -> tuple:
    return check_in_json(JSON_PATH_USERS, (login, password))
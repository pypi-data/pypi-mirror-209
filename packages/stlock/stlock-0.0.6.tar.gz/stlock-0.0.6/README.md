# Библиотека Python stlock


# Быстрый старт
Пример с библиотекой FastAPI


```
pip install stlock
pip install fastapi
pip install uvicorn
```

app.py:
```
from fastapi import FastAPI, HTTPException, Body, Query
from stlock import AuthClient


# создание экземпляра класса
AC = AuthClient(client_id="client",  # id клиента
    client_secret="secret",  # secret клиента
    code_redirect_uri="http://localhost:8000/code",  # ссылка перенаправления запроса с кодом
    service_endpoint="https://bba6q6chdp0eatf6n0ms.containers.yandexcloud.net",  # ссылка на сервис авторизации
    )


app = FastAPI()


# Регистрация пользователя
@app.post("/register", status_code=201)
def register_user(username=Body(...), password=Body(...)):
   data, status_code = AC.register(username, password)
   if status_code >= 400:
       raise HTTPException(status_code, data["detail"])
   return data


#Авторизация пользователя
@app.post('/login')
def login(username: str = Body(...), password: str = Body(...)):
   data, status_code = AC.authorize_user(username, password)
   if status_code >= 400:
       raise HTTPException(status_code, data["detail"])
   return data


@app.get('/code')
def getcode(code=Query(None)):
   data, status_code = AC.get_tokens(code)
   if status_code >= 400:
       raise HTTPException(status_code, data["detail"])
   return data
```

Для запуска сервера:
```
uvicorn app.py:app
```

# Описание методов:

    AC.register(username, password)

Создаёт нового пользователя в базе данных

    AC.authorize_user(username, password)

Авторизирует запрос на логин пользователя, перенаправляет на страницу с кодом в query запросе

    AC.get_tokens(code)

Выдаёт токены пользователя (access, refresh)

    AC.decode(token)

Декодирует токен, возвращает словарь с данными о пользователе

    AC.do_refresh(token)

Обменивает refresh token на новый access и refresh токены

# примеры запросов :
создание пользователя:
```
POST http://localhost:8000/register
Body {
    "username": "user1",
    "password": "Password123!"
}
```

Output:
```
{
    "detail": "User registred"
}
```
авторизация пользователя:
```
POST http://localhost:8000/login
Body {
    "username": "user1",
    "password": "Password123!"
}
```

Output:
```
{
    "access_token": "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJjbGllbnQiLCJleHAiOjE2ODQ3ODUwMTUsInN1YiI6ImQ5YjBmYjE1LWJjYmQtNDNkNy1hMDdlLTAxNTIwMjBlZWI2ZiIsInJvbGUiOiJUZXN0In0.kOjADrKuTmLW-MGei4VEhf9Ce16eEzgle0UVB-t_vXoMQAtMQVzdI6iK14Rmds2w1bUMh82Wwru_AmMYS2NYYQ",
    "expires_in": 60,
    "refresh_token": "ZDI5ZMUZNDETNZYYZI01OTUZLTK5MZKTNJVLMDU1OTA5MDFM",
    "token_type": "Bearer"
}
```
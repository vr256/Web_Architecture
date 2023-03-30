# Time tracking system

## About
Система Time-Tracking. Администратор закрепляет за пользователем
Активность. У пользователя может быть одна или несколько Активностей.
Пользователь отмечает кол-во затраченного времени на каждую активность.
Пользователь может отправить запрос на добавление/удаление Активности.

## Tech stack
DBMS: MySQL
Server: Waitress (pure Python WSGI server)
Builder: setuptools
Patterns: DAO, Command, MVC (MTV in Python)
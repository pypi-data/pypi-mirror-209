# RabbitMQ Broker
[![Python versions](https://img.shields.io/badge/python-%3E=3.9-blue)](https://www.python.org/)
[![Docker version](https://img.shields.io/badge/Docker-23.0.1-blue)](https://www.docker.com//)
[![](https://img.shields.io/badge/-FastAPI-green)](https://fastapi.tiangolo.com/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Isort imports](https://img.shields.io/badge/imports-isort-31674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
![coverage](http://192.168.32.52/gazprom-asez/webportal-logic/badges/develop/coverage.svg) 

Не зависящий от фреймворков пакет для общения между микросервисами. Пакет предоставляет интерфейс для работы с брокером сообщений RabbitMQ и базовый класс цепочки обработчиков.

Пакет реализует паттерн цепочка обязанностей в синхронном и асинхронном виде.

## Конфигурация

| Переменная окружения  | Описание                              |     Значение по умолчанию     |
|-----------------------|---------------------------------------|-------------------------------|
| MICROSERVICE_SETTINGS | Путь к модулю настроек проекта отно-  |         "settings"            |
|                       | -сительно корня проекта. (Разделение  |                               |
|                       | через точку: module1.module2.settings)|                               |
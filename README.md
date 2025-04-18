Название проекта:
API-сервис бронирования столиков в ресторане.

Описание:

Это REST API-сервис для бронирования столиков в ресторане, разработанный с использованием FastAPI, PostgreSQL и Docker.  
Сервис позволяет:

- Управлять столиками (создание, просмотр, удаление);
- Создавать и удалять брони;
- Исключать конфликты при бронировании.

Быстрый старт:

    Требования
    - Docker
    - Docker Compose

    Запуск проекта через консоль:
    docker-compose up --build

    После запуска API Swagger будет доступен по адресу:  
    http://localhost:8000/docs

Используемые технологии:

FastAPI, PostgreSQL, SQLAlchemy, Alembic, Docker, Pydantic, Uvicorn.

Возможности API:

	Столики

| Метод | Endpoint          | Описание                |
|-------|-------------------|-------------------------|
| GET   | /tables/          | Список всех столиков    |
| POST  | /tables/          | Создать новый столик    |
| DELETE| /tables/{id}      | Удалить столик          |

	Брони

| Метод | Endpoint            | Описание               |
|-------|---------------------|------------------------|
| GET   | /reservations/      | Список всех броней     |
| POST  | /reservations/      | Создать новую бронь    |
| DELETE| /reservations/{id}  | Удалить бронь          |


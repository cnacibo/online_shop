# 🛍️ Online Shop Project 

--- 
## Описание проекта
Это микросервисное приложение для управления 
онлайн-магазином с функционалом заказов, платежей и маршрутизацией запросов через API Gateway.


- **ApiGateway** — маршрутизирует запросы к другим сервисам.
- **OrdersService** — сервис для управления заказами.
- **PaymentsService** — сервис для управления аккаунтами, балансом и платежами.
- **Postgres** — база данных PostgreSQL с начальной инициализацией.
- **RabbitMQ** — отвечает за сообщения для асинхронной коммуникации между сервисами.

Все сервисы реализованы на FastAPI, используют PostgreSQL для хранения данных и RabbitMQ для обмена сообщениями.

---
## Структура сервисов
Каждый сервис имеет примерно такую структуру:
```
service_name/
├── app/
│   ├── api/              # REST API маршруты и эндпоинты
│   ├── domain/           # Основные сущности 
│   ├── infrastructure/   # Работа с БД, брокером сообщений и внешними ресурсами
│   ├── use_cases/        # Бизнес-логика
│   ├── schemas/          # Модели
│   └── main.py           # Точка запуска сервиса
├── Dockerfile
└── requirements.txt
```
---

## Основные API

### ApiGateway
- Перенаправляет запросы к OrdersService и PaymentsService.
- Централизует взаимодействие с клиентом.

### OrdersService
- POST /orders — создать заказ.
- GET /orders — получить список заказов пользователя.
- GET /orders/status/{order_id} — получить статус заказа.

### PaymentsService
- POST /account — создать аккаунт пользователя.
- POST /account/top-up — пополнить баланс.
- GET /account/balance — посмотреть текущий баланс.

---

## Запуск проекта

Чтобы скачать проект, выполните команду:

```
git clone https://github.com/cnacibo/online_shop
```
После этого перейдите в папку проекта:
```
cd online_shop
```
Далее необходимо запустить проект с помощью докера:

```
docker-compose up --build
```

---
## Доступ к сервисам

- **API Gateway** -> http://localhost:8000/docs#/
- **OrdersService** -> http://localhost:8001/docs#/
- **PaymentsService** -> http://localhost:8002/docs#/
- **RabbitMQ** -> http://localhost:15672/#/queues (логин/пароль - guest/guest)


Теперь все должно работать :))

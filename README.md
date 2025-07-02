# 👩🏼‍💻️ Frontend branch

--- 
## Описание проекта
Фронтенд-часть онлайн магазина, в котором можно создавать и оплачивать заказы. 

- Интерфейс реализовае на `React` и взаимодействует с бекендом через `REST API`.
- Фронтенд упакован в `Docker` контейнер и запускается через `Docker Compose` вместе
с остальными сервисами

---
## Структура frontend-части
```
frontend/  
├── public/              # Статические файлы  
├── src/  
│   ├── assets/          # Шрифты, изображения  
│   ├── components/      # Переиспользуемые UI-компоненты  
│   ├── features/        # Страницы приложения  
│   ├── store/           # State-менеджер (Redux/Zustand)  
│   ├── shared/
│   │   ├── api/
│   │   ├── styles/      # Глобальные стили           
│   └── index.tsx        # Точка входа  
├── package.json  
└── Dockerfile           
```
---


## Запуск проекта

Запуск dev-сервера:

```
npm run dev
```
Запуск для production-сборки:
```
npm run build
```

---
## Доступ к сервису

- **API Gateway** -> http://localhost:3000
- **OrdersService** -> http://localhost:3000/orders
- **PaymentsService** -> http://localhost:3000/account


Теперь все должно работать :))

# PaymentsService/app/infrastructure/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, AsyncSession
import os

# Задаем URL для подключения к базе данных
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://orders_user:orders_pass@postgres:5432/orders")

# Создание подключения к базе данных
engine = create_engine(DATABASE_URL, echo=True)

# Создаем сессию для работы с базой данных
AsyncSessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

# Базовый класс для всех моделей
Base = declarative_base()

# Функция для создания базы данных и таблиц
def create_db_and_tables():
    from app.infrastructure import repositories
    Base.metadata.create_all(bind=engine)

# Функция для получения сессии
async def get_session():
    async with AsyncSessionLocal() as session:
        yield session

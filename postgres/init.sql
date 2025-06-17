-- Создание схемы для заказов
CREATE SCHEMA IF NOT EXISTS orders;

-- Создание схемы для платежей
CREATE SCHEMA IF NOT EXISTS payments;

DO $$ BEGIN
    CREATE TYPE order_status AS ENUM ('NEW', 'PAID', 'CANCELLED');
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

-- Таблица заказов (orders.orders)
CREATE TABLE IF NOT EXISTS orders.orders (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(255),
    amount FLOAT,
    description VARCHAR(255),
    status order_status NOT NULL DEFAULT 'NEW'
);

-- Outbox-таблица для заказов (orders.outbox)
CREATE TABLE IF NOT EXISTS orders.outbox (
    id SERIAL PRIMARY KEY,
    event_type VARCHAR(255),
    payload JSONB,
    sent BOOLEAN DEFAULT FALSE
);

-- Таблица аккаунтов пользователей (payments.accounts)
CREATE TABLE IF NOT EXISTS payments.accounts (
    user_id VARCHAR(255) PRIMARY KEY,
    balance FLOAT DEFAULT 0.0
);

-- Outbox-таблица для платежей (payments.outbox)
CREATE TABLE IF NOT EXISTS payments.outbox (
    id SERIAL PRIMARY KEY,
    event_type VARCHAR(255),
    payload JSONB,
    sent BOOLEAN DEFAULT FALSE
);

-- Inbox-таблица для платежей (payments.inbox)
CREATE TABLE IF NOT EXISTS payments.inbox (
    id SERIAL PRIMARY KEY,
    event_type VARCHAR(255),
    payload JSONB,
    processed BOOLEAN DEFAULT FALSE
);

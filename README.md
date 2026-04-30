# E-Commerce Backend API

Production-style backend API built with FastAPI.

## Features

- User Authentication (JWT)
- Product Management
- Cart System
- Order Management
- Inventory Handling
- Redis Caching
- Background Tasks
- Docker Support
- Testing with Pytest

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Redis
- Docker
- Pytest

## Project Structure

app/
api/
core/
db/
models/
schemas/
services/
repositories/

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
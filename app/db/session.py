from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from app.db.init_db import init_db

engine = create_engine(settings.DATABASE_URL, echo=True)

print("DB URL:", settings.DATABASE_URL)


init_db(engine)

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
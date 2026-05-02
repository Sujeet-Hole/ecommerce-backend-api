import app.models.user

from app.db.base import Base

def init_db(engine):
    print("🔥 INIT DB CALLED")
    print("Tables found:", Base.metadata.tables.keys())  
    Base.metadata.create_all(bind=engine)
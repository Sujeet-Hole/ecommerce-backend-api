from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services import order_services

router = APIRouter()


@router.post("/orders")
def place_order(db: Session = Depends(get_db)):
    return order_services.place_order(db)
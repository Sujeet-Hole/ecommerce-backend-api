from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.cart_schema import AddToCartSchema
from app.services import cart_service


router = APIRouter()


@router.post("/add")
def add(data : AddToCartSchema , db : Session = Depends(get_db)):
    return cart_service.add_to_cart(
        user_id = data.user_id,
        product_id = data.product_id,
        quantity = data.quantity,
        db=db
    )


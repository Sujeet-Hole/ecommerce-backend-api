from app.models.order import Order
from app.models.orderitem import OrderItem
from app.models.cart import Cart


def get_cart_items(user_id, db):
    return db.query(Cart).filter(Cart.user_id == user_id).all()


def create_order(user_id, total_amount, db):
    order = Order(
        user_id=user_id,
        total_amount=total_amount,
        status="PLACED"
    )
    db.add(order)
    db.commit()
    db.refresh(order)
    return order


def create_order_item(order_id, product_id, quantity, price, db):
    item = OrderItem(
        order_id=order_id,
        product_id=product_id,
        quantity=quantity,
        price=price
    )
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def clear_cart(user_id, db):
    db.query(Cart).filter(Cart.user_id == user_id).delete()
    db.commit()

    
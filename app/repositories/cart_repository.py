from app.models.cart import Cart


def get_cart_item(user_id , product_id , db):
    return db.query(Cart).filter(Cart.user_id == user_id , Cart.product_id == product_id).first()


def create_cart_item(user_id ,product_id , quantity ,db):

    cart = Cart(
        user_id = user_id,
        product_id = product_id,
        quantity = quantity 
    )

    db.add(cart)
    db.commit()
    db.refresh(cart)

    return cart

def update_quantity(cart_item , db, quantity):

    cart_item.quantity += quantity

    db.commit()
    db.refresh(cart_item)

    return cart_item

def get_user_cart(user_id, db):
    return db.query(Cart).filter(Cart.user_id == user_id).all()

def delete_cart_item(user_id, product_id, db):
    cart_item = get_cart_item(user_id, product_id, db)
    if cart_item:
        db.delete(cart_item)
        db.commit()
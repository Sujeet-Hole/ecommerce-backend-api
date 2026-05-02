from app.repositories import cart_repository


def add_to_cart(user_id, product_id, quantity, db):
    existing_item = cart_repository.get_cart_item(user_id, product_id, quantity, db)

    if existing_item :
        return cart_repository.update_quantity(existing_item ,quantity ,db)
    
    return cart_repository.create_cart_item(user_id, product_id, quantity, db)

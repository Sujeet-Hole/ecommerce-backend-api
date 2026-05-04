from app.repositories import order_repository


def place_order(user_id , db):

    cart_item = order_repository.get_cart_items(user_id,db)

    if cart_item :
        return {"error": "Cart is empty"}
    
    total_amount = 0

    for item in cart_item :
        total_amount += item.product.price * item.quantity


    order = order_repository.create_order_(user_id ,total_amount, db)

    for item in cart_item :
         order_repository.create_order_item(
            order_id=order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=item.product.price,
            db=db
        )

    order_repository.clear_cart(user_id, db)

    return {
        "message": "Order placed successfully",
        "order_id": order.id
    }
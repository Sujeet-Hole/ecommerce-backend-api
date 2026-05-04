from pydantic import BaseModel
from datetime import datetime

class Order_Item_Schema(BaseModel):
    id : int
    order_id : int
    product_id : int
    product_name : str
    quantity : int
    unit_price : int
    total_price : int


    #  dummy schema
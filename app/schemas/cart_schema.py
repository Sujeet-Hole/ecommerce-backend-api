from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class AddToCartSchema(BaseModel):
    product_id : int
    quantity : int

    
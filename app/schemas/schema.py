from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class RegisterSchema(BaseModel):
    username  : str 
    email : str
    password : str
    
class LoginSchema(BaseModel):
    
    email : str
    password : str

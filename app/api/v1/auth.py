from fastapi import FastAPI, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from datetime import timedelta , datetime
from passlib.context import CryptContext

from app.schemas.schema import RegisterSchema, LoginSchema
from app.models.user import User
from app.db.session import get_db


router = APIRouter()

ACCESS_TOKEN_TIME = 30
SECRET_KEY = "gfhdjsktyrueiwbcnxmbbgvcnm"
algorithm = "HS256"
pwd_context = CryptContext(schemes="bcrypt" , deprecated="auto")


def create_token(data : dict):

    payload = data.copy()
    expiry = datetime.utcnow() + timedelta(minutes =ACCESS_TOKEN_TIME)
    payload.update({"exp":"expiry"})

    return jwt.encode(payload , SECRET_KEY ,algorithm=algorithm)


def hash_password(password : str):
    return pwd_context.hash(password[:72])

def verify_password(password , plain_password) :
    return pwd_context.verify(password , plain_password)

@router.post("/registration")
def register(user: RegisterSchema, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        raise HTTPException(status_code=401, detail="User already exists")

    hash_pass = hash_password(user.password)

    new_user = User(
        name=user.username,
        email=user.email,
        hashed_password=hash_pass
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "Registration successful"}
@router.post("/login")
def login(user : LoginSchema , db : Session = Depends(get_db)):

    existing_user = db.query(User).filter(User.email == user.email).first()

    if not existing_user :
        raise HTTPException(status_code=400 , detail ="user not found")
    
    verify = verify_password(user.password , existing_user.hashed_password)


    if not verify :
        raise HTTPException(status_code= 401 , detail="Invalid Credential")
    
    token = create_token(
        data={"sub": user.email}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }



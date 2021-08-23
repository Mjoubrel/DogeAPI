#!/usr/bin/python3

from typing import Optional
from datetime import timedelta, datetime
from jose import jwt
from schema.schemas import TokenData
from decouple import config

# openssl rand -hex 32
SECRET_KEY = 'jhe0lbf)365y&8(+k@c2_*)7dt(*xqnwb@a@^y_*(rn2h+*=j#'
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except jwt.Error:
        raise credentials_exception

#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config


SQLALCHEMY_DATABASE_URL = 'postgres://qciwzghywyhpmr:f36a6ae7bf3941432e03de03f1bf64983d0996403e170e84991174583b43c2c1@ec2-3-248-103-75.eu-west-1.compute.amazonaws.com:5432/dfjnvdcki6tk8k'
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={
                       "check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

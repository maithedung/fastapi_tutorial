import schemals
import models
from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from hasing import Hash


def get_all(db: Session):
    users = db.query(models.User).all()
    return users


def read(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with the id {id} is not found')
    return user


def create(request: schemals.User, db: Session):
    new_user = models.User(
        name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

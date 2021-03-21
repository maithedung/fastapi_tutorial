from database import get_db
from fastapi.params import Depends
import schemals
from typing import List
from fastapi import status
from sqlalchemy.orm import Session
from fastapi import APIRouter
from repository import user

router = APIRouter(
    prefix='/user',
    tags=['users']
)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemals.ShowUser])
def all(db: Session = Depends(get_db)):
    return user.get_all(db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemals.ShowUser)
def read(id: int, db: Session = Depends(get_db)):
    return user.read(id, db)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemals.ShowUser)
def create(request: schemals.User, db: Session = Depends(get_db)):
    return user.create(request, db)

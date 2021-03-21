from fastapi import APIRouter
from fastapi.params import Depends
import schemals
import models
from oauth2 import get_current_user
from typing import List
from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from repository import blog

router = APIRouter(
    prefix='/blog',
    tags=['blogs']
)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemals.ShowBlog])
def all(db: Session = Depends(get_db), current_user: schemals.User = Depends(get_current_user)):
    return blog.get_all(db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemals.ShowBlog)
def read(id: int, db: Session = Depends(get_db), current_user: schemals.User = Depends(get_current_user)):
    return blog.read(id, db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemals.Blog, db: Session = Depends(get_db), current_user: schemals.User = Depends(get_current_user)):
    return blog.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db), current_user: schemals.User = Depends(get_current_user)):
    return blog.delete(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemals.Blog, db: Session = Depends(get_db), current_user: schemals.User = Depends(get_current_user)):
    return blog.update(id, request, db)

import schemals
import models
from fastapi import status, HTTPException
from sqlalchemy.orm import Session


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def read(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not found')
    return blog



def create(request: schemals.Blog, db: Session):
    new_blog = models.Blog(title=request.title,
                           body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def delete(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not found')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'deleted'


def update(id: int, request: schemals.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not found')
    blog.update(request)
    db.commit()
    return 'updated'

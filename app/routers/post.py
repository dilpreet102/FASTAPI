from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter

from app import models, schemas, oauth2
from sqlalchemy.orm import Session
from app.database import get_db
from typing import List, Optional

router = APIRouter(
    prefix="/posts",
    tags=['Post']
)

@router.get("/", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit : int = 10, skip: int = 0, search: Optional[str] = ""):
    # cur.execute("SELECT * from posts")
    # posts = cur.fetchall()
    print(limit)
    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    return posts


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db),
                 current_user: int = Depends(oauth2.get_current_user)):
    # cur.execute("INSERT INTO posts(title, content, published) VALUES (? , ? , ?) ", (new_post.title, new_post.content, new_post.published))
    # post = cur.fetchone()
    # connection.commit()
    new_post = models.Post(owner_id = current_user.id , **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


@router.get("/{id}", response_model=schemas.Post)
def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cur.execute("SELECT * FROM posts WHERE id = ?", (str(id),))
    # post = cur.fetchone()
    post = db.query(models.Post).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} not found")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorised to perform requested action")

    return post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cur.execute("delete from posts where id = ? ", (str(id),))
    # deleted_post = cur.fetchone()
    # connection.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post== None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorised to perform requested action")

    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cur.execute("update posts set title = ? , content = ? , published = ? where id = ? ", (post.title, post.content, post.published, str(id)))
    # updated_post = cur.fetchone()
    # connection.commit()

    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorised to perform requested action")

    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()
from fastapi import FastAPI, HTTPException, Response, Depends, APIRouter, status

from .. import models
from .. import schema, oauth2
from..database import get_db
from sqlalchemy.orm import session

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.get("/")
async def get_posts(db: session= Depends(get_db),  current_user: int= Depends(oauth2.get_current_user), limit:int= 10, skip:int= 0 ):
    
    posts=db.query(models.Post).filter(models.Post.owner_id== current_user.id).limit(limit).offset(skip).all() # now only logged in user post is visible with specific user_id
    return {"posts": posts}


@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_post(post: schema.Post, db: session = Depends(get_db), current_user: int= Depends(oauth2.get_current_user)):
    new_post = models.Post(owner_id= current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"post": new_post}

@router.get("/{id}")  # this id is in string 
async def get_post(id: int, response: Response, db: session= Depends(get_db)):
        
        posts= db.query(models.Post).filter(models.Post.id==id).first()
        if not posts:
            raise HTTPException(status_code=404, detail="Post not found")
        return {"post": posts}
   
    

@router.delete("/{id}")
async def delete_post(id: int, db: session= Depends(get_db), current_user: schema.UserResponse = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    if post.owner_id != int(current_user.id):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")
    db.delete(post)
    db.commit()
    return {"message": "Post deleted successfully"}

    

@router.put("/{id}")
async def update_post(id: int, post: schema.Post, db: session = Depends(get_db), current_user: schema.UserResponse = Depends(oauth2.get_current_user)):
    update_post= db.query(models.Post).filter(models.Post.id==id).first()

    if update_post == None:
        raise HTTPException(status_code=404, detail="Post not found")
    if update_post.owner_id != int(current_user.id):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")
    
    update_data = post.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(update_post, key, value)
        db.commit()
    return {"message": "Post has been updated successfully"}
    



from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .models import Todo, TodoCreate, TodoItem, TodoUpdate
from .database import get_db

router = APIRouter()

@router.get("/api/healthchecker")
def healthchecker():
    return {"status": "success", "message": "Integrate FastAPI Framework with Next.js"}

@router.post("/api/todos", response_model=TodoItem)
def create_todo_item(todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = Todo(title=todo.title)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@router.get("/api/todos", response_model=list[TodoItem])
def get_all_todo_items(db: Session = Depends(get_db)):
    return db.query(Todo).all()

@router.patch("/api/todos/{todo_id}", response_model=TodoItem)
def update_todo_item(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo item not found")
    
    if todo.title is not None:
        db_todo.title = todo.title
    if todo.completed is not None:
        db_todo.completed = todo.completed
    
    db.commit()
    db.refresh(db_todo)
    return db_todo

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import crud
import schemas
from database import engine, get_db
from models import Base

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://employee-management-ui.onrender.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {
        "message": "Welcome to Employee Management API"
    }


@app.get("/employees", response_model=list[schemas.EmployeeResponse])
def get_employees(db: Session = Depends(get_db)):
    print("GET /employees called")
    employees = crud.get_employees(db)
    print(employees)
    return employees


@app.post("/employees", response_model=schemas.EmployeeResponse)
def create_employee(
    employee: schemas.EmployeeCreate,
    db: Session = Depends(get_db)
):
    return crud.create_employee(db, employee)
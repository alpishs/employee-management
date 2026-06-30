from sqlalchemy.orm import Session
import models
import schemas


def get_employees(db: Session):
    return db.query(models.Employee).all()

def create_employee(db: Session, employee: schemas.EmployeeCreate):

    db_employee = models.Employee(
        name=employee.name,
        role=employee.role
    )

    db.add(db_employee)

    db.commit()

    db.refresh(db_employee)

    return db_employee

def get_employee(db: Session, employee_id: int):
    return (
        db.query(models.Employee)
        .filter(models.Employee.id == employee_id)
        .first()
    )
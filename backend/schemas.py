from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    name: str
    role: str


class EmployeeResponse(EmployeeCreate):
    id: int

    class Config:
        from_attributes = True
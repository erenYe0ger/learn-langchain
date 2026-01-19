from pydantic import BaseModel, Field
from typing import Optional

class Student(BaseModel):
    name: str = 'default_name'
    age: Optional[int] = None
    marks: float = Field(gt=50, lt=90, description='total marks of the student', default=67)

student1 = {
    'age': 60,
    'name': 'Elon'
}

print(Student(**student1))
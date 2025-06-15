from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class stident(BaseModel):
    name:str ='nitish'
    age:Optional[int]=None
    email:EmailStr
    cgpa:float=Field(gt=0,lt=10,default=8,description='A decimal value ')

new_student={'age':'32','email':'abc@gmail.com','cgpa':5}

student=stident(**new_student)


print(student)
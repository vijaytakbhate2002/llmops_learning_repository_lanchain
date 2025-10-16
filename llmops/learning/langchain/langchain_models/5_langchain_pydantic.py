# Pydantic Validation:
# BaseModel: Used to create pydantic dictionary which can throw error if there is type missmatch in input data
# EmailStr (hint): Used to validate email before storing email into variable
# Field (Hint): you can add min and max range that variable can store

from langchain_openai import ChatOpenAI
from typing import TypedDict, Optional
from pydantic import BaseModel, EmailStr, Field
from dotenv import load_dotenv

load_dotenv()

# model = ChatOpenAI(
#     name='gpt-5-mini',
#     temperature=0.7
# )

class QuestionClass(BaseModel):
    question: Optional[str] = None
    response_numbers: int 
    email: EmailStr
    age:float = Field(gt=18, lt=60)

temp = {'response_numbers':24, 'email':"takbhate@gmail.com", "age":65}

print(QuestionClass(**temp))
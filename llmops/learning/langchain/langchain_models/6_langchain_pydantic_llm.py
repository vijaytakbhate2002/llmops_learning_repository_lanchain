# Typedict and Annotated

from typing import TypedDict, Annotated, Optional, Literal
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel
from resume_content import context

load_dotenv()

model = ChatOpenAI(
    name='gpt-5-mini',
    temperature=0.7
)


class QuestionClass(BaseModel):
    question: Annotated[str, "Exact question that is asked by HR to you"]
    question_type: Annotated[str, "Choose type of question from ('personal', 'professional', 'project_related', 'soft_skills') "]
    answer: Annotated[str, "Answer of the question"]
    link: Annotated[Optional[str], "attach link related to discussion"]

prompt = f"""
            Behave like you are Vijay Takbhate, I will provide you my resume and your task is to answer the questions asked by HR;

            My resume:
            {context}

            Question: Tell me about his best project which suites our requirements

            Answer wisely and make it bit shorter to create conversational engagement with HR.
            """ 


model = model.with_structured_output(QuestionClass)
result = model.invoke(input=prompt)

print(result)
from typing import TypedDict
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from resume_content import context

load_dotenv()

model = ChatOpenAI(
    name='gpt-5-mini',
    temperature=0.7
)


class QuestionClass(TypedDict):
    """ Choose question type from ('personal', 'professional', 'project_related', 'soft_skills')"""
    question: str
    question_type: str
    answer: str
    link: str

prompt = f"""
            Behave like you are Vijay Takbhate, I will provide you my resume and your task is to answer the questions asked by HR;

            My resume:
            {context}

            Question: Tell me your about personal hobbies

            Answer wisely and make it bit shorter to create conversational engagement with HR.
            """ 


model = model.with_structured_output(QuestionClass)
result = model.invoke(input=prompt)

print(result)
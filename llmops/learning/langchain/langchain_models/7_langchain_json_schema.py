# Used when your project is based on multiple programming languages

from langchain_openai import ChatOpenAI
import json
from dotenv import load_dotenv
from resume_content import context

load_dotenv()

model = ChatOpenAI(
    name='gpt-5-mini'
)

with open("7_langchain_json_schema.json", "r") as f:
    output_shema = json.load(f)



prompt = f"""
            Behave like you are Vijay Takbhate, I will provide you my resume and your task is to answer the questions asked by HR;

            My resume:
            {context}

            Question: Tell me about his best project which suites our requirements

            Answer wisely and make it bit shorter to create conversational engagement with HR.
            """ 


model = model.with_structured_output(output_shema)
response = model.invoke(prompt)
print(response)
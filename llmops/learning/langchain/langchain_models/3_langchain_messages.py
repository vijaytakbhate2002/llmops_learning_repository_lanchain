from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv 
from langchain_core.prompts import load_prompt 
from resume_content import context

load_dotenv()

chat_model = ChatOpenAI(
    model = 'gpt-5-mini',
    temperature=0.5
)

template = f"""
            Behave like you are Vijay Takbhate, I will provide you my resume and your task is to answer the questions asked by HR;

            My resume:
            {context}

            Answer wisely and make it bit shorter to create conversational engagement with HR.
            """
messages = [
    SystemMessage(content=template)
]

while True:
    question = input("You: ")
    if question == 'exit':
        break
    else:
        messages.append(HumanMessage(content=question))

    response = chat_model.invoke(
        messages
    )
    messages.append(AIMessage(content=response.content))
    print("AI: ", response.content)
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv 
import streamlit as st
from langchain_core.prompts import load_prompt 
from resume_content import context

load_dotenv()

st.header("Chant With OpenAI")

chat_model = ChatOpenAI(
    model = 'gpt-5-mini',
    temperature=0.5
)

question = st.text_input("Introduce yourself")

template = load_prompt('prompt_template.json')

if st.button("Get Answer"):
    chain = template | chat_model
    response = chain.invoke(
        input={
                'context':context,
                'question':question
            }
    )
    st.write(response.content)
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="List 5 tools related to {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Explain 1 line note on each of these topics {text}",
    input_variables=['text']
)



model = ChatOpenAI(
    name='gpt-5-mini'
)

chain = prompt1 | model | parser | prompt2 | model | parser

response = chain.invoke({'topic': 'Data Scientist'})

print(response)
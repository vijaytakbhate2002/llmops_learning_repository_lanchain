from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()


prompt = PromptTemplate(
    template="Give me top 5 tools required for {topic}",
    input_variables=['topic'],

)

model = ChatOpenAI(
    name='gpt-5-mini'
)


parser = StrOutputParser()

chain = prompt | model | parser

response = chain.invoke({'topic': "Roadmap of Data Scientist"})

print(response)
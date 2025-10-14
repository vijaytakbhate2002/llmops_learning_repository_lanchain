from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

# Initialize Chat model
chat_model = ChatOpenAI(
    model="gpt-5-mini",  
    temperature=0.7
)

# Prompt template (works with ChatOpenAI)
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in 4 lines."
)

# Chain
chain = prompt | chat_model

# Run
response = chain.invoke({"topic": "langchain"})
print(response.content)

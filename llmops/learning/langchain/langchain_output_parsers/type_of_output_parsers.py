# ✅ Step 1: Import necessary libraries
from langchain.prompts import PromptTemplate
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# ✅ Step 2: Initialize the model
model = ChatOpenAI(model="gpt-5-mini", temperature=0.5)

# ✅ Step 3: Initialize the parser
parser = CommaSeparatedListOutputParser()

print(parser.get_format_instructions())

# ✅ Step 4: Create a prompt template
prompt = PromptTemplate(
    template=(
        "List five important concepts related to {topic}.\n"
       
    ),
    input_variables=["topic"],  # user-provided
    partial_variables={          # pre-filled, system-provided
        "format_instructions": parser.get_format_instructions()
    }
)

# ✅ Step 5: Combine prompt, model, and parser into one chain
chain = prompt | model | parser

# ✅ Step 6: Ask user for a topic (you can replace this with a variable)
user_input = {"topic": "Data Scientist"}

# ✅ Step 7: Run the chain
response = chain.invoke(user_input)

# ✅ Step 8: Print the parsed result
print(response)

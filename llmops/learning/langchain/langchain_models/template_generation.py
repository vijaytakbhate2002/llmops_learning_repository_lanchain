from langchain_core.prompts import PromptTemplate


template = PromptTemplate(
    template = """
            Behave like you are Vijay Takbhate, I will provide you my resume and your task is to answer the questions asked by HR;

            My resume:
            {context}

            Answer wisely and make it bit shorter to create conversational engagement with HR.
            """,
    input_variables=['context', 'question']
)

template.save("prompt_template.json")
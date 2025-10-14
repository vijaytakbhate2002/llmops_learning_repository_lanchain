from huggingface_hub import InferenceClient
from resume_context import resume_qa, context_compressed
import os

# client = InferenceClient(api_key=os.environ.get('TOKEN'))

# for model in chat_completion_models:
#     try:
#         print("===========================", model, "=================================")
#         for question, answer in resume_qa.items():
#             response = client.chat_completion(
#                 model=model,
#                 messages=[
#                     {"role": "user", "content": "Based on my resume content please answer questions that I have asked to you. Resume content start from here: " + context_compressed + " Resume content ends here, question: "+ question + " please give me short answer"}
#                 ],
#             )
#             print(response.choices[0].message.content)
#             print("===========================", answer, "=================================")
#             break
#     except Exception as e:
#         print(e)



import requests
import os
import time

YOUR_GROQ_API_KEY = os.environ.get('GROG_API')

for question, answer in resume_qa.items():
    headers = {"Authorization": f"Bearer {YOUR_GROQ_API_KEY}"}
    payload = {
    "model": "llama-3.3-70b-versatile",
    "messages": [{"role": "user", "content": "Based on my resume content please answer questions that I have asked to you. Resume content start from here: \n" + context_compressed + " \nResume content ends here, question:\n "+ question + "Note: HR will ask these questions to you when I deploy you on aws so answer wisely"}]
    }

    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
    model_response = response.json()["choices"][0]["message"]["content"]
    print("+++++++++++++++++++++++++++++++ Question ++++++++++++++++++++++++++++")
    print(question)
    print("+++++++++++++++++++++++++++++++ Model Response ++++++++++++++++++++++++++++")
    print(model_response)
    print("+++++++++++++++++++++++++++++++ Correct Answer ++++++++++++++++++++++++++++")
    print(answer)
    time.sleep(3)

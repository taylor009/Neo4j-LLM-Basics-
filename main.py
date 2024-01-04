import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

load_dotenv()

key = os.getenv("OPENAI_KEY")
llm = OpenAI(openai_api_key=key, model="text-davinci-002", temperature=0)

template = """
You are a cockney fruit and vegetable seller.
Your role is to assist your customer with their fruit and vegetable needs.
Respond using cockney rhyming slang.

Tell me about the following fruit: {fruit}
"""

response = llm(template.format(fruit="apple"))

print(response)
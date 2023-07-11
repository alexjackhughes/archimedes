import openai
import pinecone
import numpy as np
import os

from dotenv import load_dotenv
load_dotenv()

openai.organization = os.getenv("OPENAI_ORGANIZATION_ID")
openai_api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = openai_api_key

model = os.environ.get("CHAT_MODEL")

def generate_completion(prompt):
  response = openai.ChatCompletion.create(
    model=model,
    messages=[
          # Potentially messages here should be added depending on the context of the conversation  
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": "Who won the world series in 2020?"},
          {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
          {"role": "user", "content": prompt}
      ]
    )

  return response['choices'][0]['message']['content']
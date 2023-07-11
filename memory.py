import openai
import pinecone
import numpy as np
import os

from dotenv import load_dotenv
load_dotenv()

openai.organization = os.getenv("OPENAI_ORGANIZATION_ID")
openai_api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = openai_api_key

pinecone_api_key = os.environ.get("PINECONE_API_KEY")
model = os.environ.get("EMBEDDING_MODEL")
environment = os.environ.get("PINECONE_ENV")
index_name = os.environ.get("PINECONE_INDEX")

pinecone.init(api_key=pinecone_api_key, environment=environment)

class MemoryStore:
    def __init__(self):
        self.index = pinecone.Index(index_name=index_name)

    def store_thought(self, thought_string):
        # Use an AI model to convert the thought string into a vector
        thought_vector = self.embed_thought(thought_string)

        # Store the thought in the vector database
        self.index.upsert([(thought_string, thought_vector.tolist())])

    def retrieve_thought(self, query_string):
        # Use an AI model to convert the query string into a vector
        query_vector = self.embed_thought(query_string)

        # Query the vector database
        results = self.index.query(vector=query_vector.tolist(), top_k=1, include_values=True)

        # Return the ID of the most relevant thought
        return results['matches'][0]['id']

    def embed_thought(self, text):
      response = openai.Embedding.create(
          input=[text],  # Put the text in a list here
          model=model
      )
      embeddings = response['data'][0]['embedding']
      return np.array(embeddings)  # Convert the list of embeddings to a numpy array
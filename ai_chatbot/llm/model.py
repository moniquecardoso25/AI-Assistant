import os
from langchain_openai import ChatOpenAI

def get_llm(*, temperature: float=0.7):
    """
    Returns a ChatOpenAI instance with specified temperature.
    Temperature controls the randomness of the model's output.
    Returns instance
    """
        
    return ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0,
        openai_api_key=os.getenv("OPENAI_API_KEY"),
    )


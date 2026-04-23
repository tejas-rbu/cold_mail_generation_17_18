import os
from groq import Groq

def get_client():
    return Groq(api_key=os.environ["GROQ_API_KEY"])
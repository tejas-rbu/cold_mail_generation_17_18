import os
from groq import Groq
from tavily import TavilyClient


# ---------------- GROQ ----------------
def get_client():
    return Groq(api_key=os.getenv("GROQ_API_KEY"))


# ---------------- TAVILY ----------------
def search_web(query):

    client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

    response = client.search(
        query=query,
        search_depth="basic"
    )

    results = response.get("results", [])

    context = "\n".join(
        [f"{r.get('title')} - {r.get('content')}" for r in results[:5]]
    )

    return context

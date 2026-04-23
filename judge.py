from tools import get_client

client = get_client()

MODEL = "llama-3.3-70b-versatile"


def evaluate_email(email):

    prompt = f"""
    Evaluate email:

    Email:
    {email}

    Give:
    Hook /10
    Relevance /10
    Clarity /10
    CTA /10
    Total /40
    Feedback
    """

    res = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return res.choices[0].message.content

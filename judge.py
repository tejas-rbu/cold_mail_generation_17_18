from tools import get_client

client = get_client()

MODEL = "llama-3.3-70b-versatile"


def evaluate_email(email):

    prompt = f"""
    Evaluate this cold email:

    Score on:
    - Clarity (10)
    - Personalization (10)
    - Persuasion (10)
    - CTA (10)

    Give total out of 40 and improvements.

    Email:
    {email}
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a strict AI sales email reviewer."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
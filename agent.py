from tools import get_client, search_web

client = get_client()

MODEL = "llama-3.3-70b-versatile"


def define_persona(industry, product, role):

    context = search_web(f"{industry} {product}")

    prompt = f"""
    Use this real-world context:
    {context}

    Create buyer persona.

    Industry: {industry}
    Product: {product}
    Role: {role}

    Include:
    - Job role
    - Pain points
    - Goals
    - Buying triggers
    """

    res = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return res.choices[0].message.content


def generate_email(persona, product):

    prompt = f"""
    Write a cold email.

    Persona:
    {persona}

    Product:
    {product}

    Keep it short and persuasive.
    """

    res = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return res.choices[0].message.content

from tools import get_client

client = get_client()

MODEL = "llama-3.3-70b-versatile"


def define_persona(industry, product):

    prompt = f"""
    Define a detailed buyer persona.

    Industry: {industry}
    Product: {product}

    Include:
    - Job role
    - Pain points
    - Goals
    - Buying triggers
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a B2B marketing strategist."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


def generate_email(persona, product):

    prompt = f"""
    Write a persuasive cold email.

    Persona:
    {persona}

    Product:
    {product}

    Make it short, personalized and include CTA.
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are an expert cold email copywriter."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
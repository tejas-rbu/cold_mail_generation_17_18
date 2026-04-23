import streamlit as st
from agent import define_persona, generate_email
from judge import evaluate_email

st.title("🚀 AI Cold Email Generator (Groq Powered)")

industry = st.text_input("Industry")
product = st.text_input("Product")

if st.button("Generate Email"):

    with st.spinner("Generating persona..."):
        persona = define_persona(industry, product)

    with st.spinner("Generating email..."):
        email = generate_email(persona, product)

    with st.spinner("Evaluating email..."):
        evaluation = evaluate_email(email)

    st.subheader("🧠 Persona")
    st.write(persona)

    st.subheader("✉️ Email")
    st.write(email)

    st.subheader("📊 Evaluation")
    st.write(evaluation)

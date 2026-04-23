import streamlit as st
from agent import define_persona, generate_email
from judge import evaluate_email

st.set_page_config(page_title="Outreach AI", layout="wide")

st.title("🚀 Outreach AI (Multi-Agent System)")

industry = st.text_input("Industry")
product = st.text_input("Product")
role = st.text_input("Target Role (optional)")

if "history" not in st.session_state:
    st.session_state.history = []

def run_pipeline(industry, product, role):

    persona = define_persona(industry, product, role)
    email = generate_email(persona, product)
    evaluation = evaluate_email(email)

    return persona, email, evaluation


if st.button("Generate Cold Email 🚀"):

    if not industry or not product:
        st.error("Please fill Industry and Product")
    else:
        try:
            with st.spinner("Running AI agents..."):
                persona, email, evaluation = run_pipeline(industry, product, role)

            st.success("Generated Successfully!")

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("🧠 Persona")
                st.write(persona)

            with col2:
                st.subheader("📊 Evaluation")
                st.write(evaluation)

            st.subheader("✉️ Email")
            st.code(email)

            st.session_state.history.append({
                "industry": industry,
                "product": product,
                "email": email
            })

        except Exception as e:
            st.error(f"Error: {str(e)}")


st.divider()
st.subheader("📁 History")

for item in reversed(st.session_state.history[-5:]):
    st.write(f"{item['industry']} → {item['product']}")
    st.code(item["email"])

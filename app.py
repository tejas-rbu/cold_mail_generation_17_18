import streamlit as st
from agent import define_persona, generate_email
from judge import evaluate_email

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="AI Cold Email Generator",
    page_icon="🚀",
    layout="wide"
)

# ---------------------------
# CUSTOM CSS (UI UPGRADE)
# ---------------------------
st.markdown("""
<style>

.main {
    background-color: #0f172a;
}

h1, h2, h3 {
    color: #ffffff;
}

.stTextInput > div > div > input {
    padding: 12px;
    border-radius: 10px;
}

.stButton > button {
    background-color: #4f46e5;
    color: white;
    padding: 10px 20px;
    border-radius: 10px;
    font-weight: bold;
    border: none;
}

.stButton > button:hover {
    background-color: #4338ca;
}

.block-container {
    padding-top: 2rem;
}

.card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 15px;
    margin-top: 10px;
}

.small-text {
    color: #94a3b8;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------
# HEADER
# ---------------------------
st.title("🚀 AI Cold Email Generator")
st.markdown("<p class='small-text'>Powered by Groq + Multi-Agent AI System</p>", unsafe_allow_html=True)

st.divider()

# ---------------------------
# INPUT SECTION
# ---------------------------
col1, col2 = st.columns(2)

with col1:
    industry = st.text_input("🏢 Industry", placeholder="e.g. SaaS, Fintech, Healthcare")

with col2:
    product = st.text_input("📦 Product", placeholder="e.g. CRM tool, AI software")

generate = st.button("🚀 Generate Cold Email")

# ---------------------------
# SESSION STATE (history)
# ---------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# ---------------------------
# MAIN LOGIC
# ---------------------------
if generate:

    if not industry or not product:
        st.error("Please fill both Industry and Product fields")
    else:

        with st.spinner("🧠 Creating buyer persona..."):
            persona = define_persona(industry, product)

        with st.spinner("✉️ Writing cold email..."):
            email = generate_email(persona, product)

        with st.spinner("📊 Evaluating email quality..."):
            evaluation = evaluate_email(email)

        # Save history
        st.session_state.history.append({
            "industry": industry,
            "product": product,
            "email": email
        })

        # ---------------------------
        # OUTPUT UI
        # ---------------------------
        st.success("Generated Successfully!")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("## 🧠 Persona")
            st.markdown(f"<div class='card'>{persona}</div>", unsafe_allow_html=True)

        with col2:
            st.markdown("## 📊 Evaluation")
            st.markdown(f"<div class='card'>{evaluation}</div>", unsafe_allow_html=True)

        st.markdown("## ✉️ Generated Email")
        st.markdown(f"<div class='card'>{email}</div>", unsafe_allow_html=True)

        st.code(email, language="text")

# ---------------------------
# HISTORY SECTION
# ---------------------------
st.divider()

st.subheader("📁 Previous Generations")

if st.session_state.history:

    for i, item in enumerate(reversed(st.session_state.history[-5:])):

        with st.expander(f"{item['industry']} → {item['product']}"):

            st.write(item["email"])

            st.download_button(
                label="⬇️ Download Email",
                data=item["email"],
                file_name=f"cold_email_{i}.txt"
            )
else:
    st.info("No history yet. Generate your first email 🚀")

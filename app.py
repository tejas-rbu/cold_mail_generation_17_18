import streamlit as st
from agent import define_persona, generate_email
from judge import evaluate_email

# -----------------------
# PAGE CONFIG
# -----------------------
st.set_page_config(
    page_title="Outreach AI",
    page_icon="🚀",
    layout="wide"
)

# -----------------------
# CSS (Premium SaaS UI)
# -----------------------
st.markdown("""
<style>

body {
    background-color: #09090b;
}

.main {
    background-color: #09090b;
}

h1, h2, h3 {
    color: #fafafa;
    font-family: 'DM Sans', sans-serif;
}

.block-container {
    padding-top: 2rem;
}

/* Card style */
.card {
    background-color: #18181b;
    border: 1px solid #27272a;
    padding: 16px;
    border-radius: 12px;
    margin-bottom: 12px;
}

/* Inputs */
.stTextInput input {
    background-color: #18181b;
    color: white;
    border: 1px solid #27272a;
    padding: 10px;
    border-radius: 8px;
}

/* Button */
.stButton > button {
    width: 100%;
    background-color: #7c3aed;
    color: white;
    padding: 12px;
    border-radius: 8px;
    border: none;
    font-weight: 500;
}

.stButton > button:hover {
    background-color: #6d28d9;
}

/* Muted text */
.small {
    color: #71717a;
    font-size: 13px;
}

/* Pipeline dots */
.dot {
    height: 8px;
    width: 8px;
    background-color: #27272a;
    border-radius: 50%;
    display: inline-block;
    margin-right: 6px;
}

.active {
    background-color: #7c3aed;
}

</style>
""", unsafe_allow_html=True)

# -----------------------
# HEADER
# -----------------------
st.title("🚀 Outreach AI")
st.markdown("<p class='small'>Multi-agent cold email generator powered by Groq</p>", unsafe_allow_html=True)

st.divider()

# -----------------------
# INPUT UI
# -----------------------
col1, col2 = st.columns(2)

with col1:
    industry = st.text_input("Industry")

with col2:
    product = st.text_input("Product")

role = st.text_input("Target Role (optional)")

run = st.button("🚀 Generate Cold Email")

# -----------------------
# SESSION STATE
# -----------------------
if "history" not in st.session_state:
    st.session_state.history = []

# -----------------------
# PIPELINE VISUAL
# -----------------------
def pipeline(step):
    st.markdown("### Pipeline Status")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("Persona " + ("🟣" if step>=1 else "⚪"))

    with col2:
        st.markdown("Email " + ("🟣" if step>=2 else "⚪"))

    with col3:
        st.markdown("Evaluation " + ("🟣" if step>=3 else "⚪"))

# -----------------------
# MAIN LOGIC
# -----------------------
if run:

    if not industry or not product:
        st.error("Please fill Industry and Product")
    else:

        # STEP 1
        pipeline(1)
        with st.spinner("Generating persona..."):
            persona = define_persona(industry, product)

        # STEP 2
        pipeline(2)
        with st.spinner("Writing email..."):
            email = generate_email(persona, product)

        # STEP 3
        pipeline(3)
        with st.spinner("Evaluating..."):
            evaluation = evaluate_email(email)

        # save history
        st.session_state.history.append({
            "industry": industry,
            "product": product,
            "email": email
        })

        st.success("Generated Successfully 🚀")

        # -----------------------
        # RESULTS
        # -----------------------
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 🧠 Persona")
            st.markdown(f"<div class='card'>{persona}</div>", unsafe_allow_html=True)

        with col2:
            st.markdown("### 📊 Evaluation")
            st.markdown(f"<div class='card'>{evaluation}</div>", unsafe_allow_html=True)

        st.markdown("### ✉️ Cold Email")
        st.markdown(f"<div class='card'>{email}</div>", unsafe_allow_html=True)

        st.code(email)

# -----------------------
# HISTORY SECTION
# -----------------------
st.divider()
st.markdown("### 📁 Recent Generations")

if st.session_state.history:

    for item in reversed(st.session_state.history[-5:]):
        st.markdown(
            f"<div class='card'>{item['industry']} → {item['product']}<br><br>{item['email']}</div>",
            unsafe_allow_html=True
        )
else:
    st.info("No history yet")

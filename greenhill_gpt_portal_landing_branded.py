
import streamlit as st
import openai
import os

# Configure page
st.set_page_config(page_title="Green Hill GPT – Investor Assistant", page_icon="🌿", layout="wide")

# Load logo
st.image("logo.png", width=120)

# Main header
st.markdown(
    "<h1 style='color: #1B4332; font-size: 36px;'>Green Hill GPT Investor Assistant</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='font-size: 18px; color: #2E7D32;'>Interact directly with our strategic plan. Ask about financials, board structure, GMP processes, and investor protections – all powered by our AI-native system.</p>",
    unsafe_allow_html=True
)

# Sample prompt selection
st.markdown("### 💡 Suggested Questions")
example_prompts = [
    "What’s the projected ROI by 2029?",
    "Where is the board control clause in the SHA?",
    "Summarize the CAPEX requirements.",
    "How does freeze-drying benefit the product?",
    "Explain the ZEC tax advantage.",
    "Summarize investor protections in the agreement."
]
selected = st.selectbox("Choose a question or ask your own:", [""] + example_prompts)

# Style buttons
st.markdown("""
    <style>
    .stButton>button {
        background-color: #1B4332;
        color: white;
        font-weight: bold;
        border-radius: 6px;
        padding: 0.5em 1em;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# Input form
with st.form("ask_gpt_form"):
    user_query = st.text_input("✍️ Type your question below:", value=selected if selected else "")
    submitted = st.form_submit_button("Ask GPT")

# OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

if submitted and user_query.strip():
    with st.spinner("Thinking..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are the Green Hill GPT Assistant, trained on the 2025 Strategic Plan for Green Hill Canarias. Provide investor-grade answers, with strategic insights and references where appropriate."},
                    {"role": "user", "content": user_query}
                ]
            )
            st.markdown("### ✅ Answer")
            st.write(response.choices[0].message["content"])
        except Exception as e:
            st.error(f"An error occurred: {e}")


import streamlit as st
import openai
import os

# Set your OpenAI API key (use env variable for security)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Custom branding
st.set_page_config(page_title="Green Hill GPT – Investor Assistant", page_icon="🌿")

# Header and logo
st.markdown(
    "<div style='display: flex; align-items: center;'>"
    "<img src='https://1drv.ms/u/s!Aq1kUIGXQ5Ki3Yt5X6aXWJ6cFqQ1?e=RxTJ90' width='80' style='margin-right: 15px;'>"
    "<h1 style='color: #2E7D32;'>Green Hill GPT Investor Assistant</h1></div>",
    unsafe_allow_html=True
)

st.markdown("### 💬 Ask your questions about the 2025 Strategic Plan")

# Preloaded questions section
st.markdown("#### 🧠 Suggested Investor Prompts:")
example_questions = [
    "What’s the projected ROI by 2029?",
    "Where is the board control clause in the SHA?",
    "Explain the freeze-drying advantage.",
    "Summarize the CAPEX requirements.",
    "What protections do Class B shareholders have?",
    "Show me the executive summary."
]
selected_prompt = st.selectbox("💡 Choose a sample question or type your own:", [""] + example_questions)

# Custom colors
st.markdown("""
<style>
    .stButton>button {
        background-color: #2E7D32;
        color: white;
        font-weight: bold;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Input form
with st.form("ghc_question_form"):
    user_question = st.text_input("✍️ Type your question below:", value=selected_prompt if selected_prompt else "")
    submitted = st.form_submit_button("Ask Green Hill GPT")

if submitted and user_question.strip():
    with st.spinner("🔍 Thinking..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are the Green Hill GPT Assistant, trained on the 2025 Strategic Plan. Provide precise, investor-ready answers with references where appropriate."},
                    {"role": "user", "content": user_question}
                ]
            )
            st.success(response.choices[0].message["content"])
        except Exception as e:
            st.error(f"An error occurred while contacting OpenAI: {e}")

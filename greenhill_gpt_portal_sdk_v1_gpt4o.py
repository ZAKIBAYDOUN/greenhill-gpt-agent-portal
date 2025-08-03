
import streamlit as st
import openai
import os

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="Green Hill GPT – Investor Assistant", page_icon="🌿", layout="wide")
st.image("logo.png", width=120)

st.markdown(
    "<h1 style='color: #1B4332; font-size: 36px;'>Green Hill GPT – Investor Assistant</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='font-size: 18px; color: #2E7D32;'>Ask questions about Green Hill Canarias’ strategic plan, SHA, GMP compliance, CAPEX, or cultivation model.</p>",
    unsafe_allow_html=True
)

prompts = [
    "What’s the yield per flowering room?",
    "Where is freeze-drying implemented?",
    "How is shareholder governance structured?",
    "What is the CAPEX breakdown for GMP equipment?",
    "What are the cultivation model assumptions?",
]
selected_prompt = st.selectbox("💡 Choose a question or ask your own:", [""] + prompts)

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

with st.form("ghc_form"):
    question = st.text_input("✍️ Type your question below:", value=selected_prompt if selected_prompt else "")
    submitted = st.form_submit_button("Ask GPT")

if submitted and question.strip():
    with st.spinner("Thinking..."):
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": (
                        "You are the Green Hill GPT Assistant. You support investor queries based on the 2025 Strategic Plan, "
                        "SHA (Shareholder Agreement), and Conceptual GMP facility design. Prioritize clarity, structure, and alignment "
                        "with EU-GMP standards. Clarify freeze-drying is used for pharmaceutical-grade post-harvest stabilization, "
                        "not food. Yield assumptions are 500 g/m² with 4×25 kg lots per cycle, per flowering room — based on validated "
                        "cultivation modeling. The engineering document MEM-03.00 used 315 g/m² and 3 lots as placeholders. Use references "
                        "when possible and respond in investor-grade tone."
                    )},
                    {"role": "user", "content": question}
                ]
            )
            st.markdown("### ✅ Answer")
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"An error occurred: {e}")

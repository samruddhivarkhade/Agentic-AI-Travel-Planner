import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

import streamlit as st
from agent.travel_agent import run_travel_agent_demo
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

bg_image = get_base64_image("assets/travel_bg.jpg")

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Agentic AI Travel Planner",
    page_icon="✈️",
    layout="centered"
)

# ---------------- CUSTOM CSS ---------------- #
st.markdown(f"""
<style>
.stApp {{
    background-image: linear-gradient(
        rgba(0, 0, 0, 0.45),
        rgba(0, 0, 0, 0.45)
    ),
    url("data:image/jpg;base64,{bg_image}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

.main-title {{
    text-align: center;
    font-size: 2.4rem;
    font-weight: 700;
    color: #ffffff;
}}

.sub-title {{
    text-align: center;
    color: #e5e7eb;
    margin-bottom: 30px;
}}

.card {{
    background: rgba(255, 255, 255, 0.95);
    padding: 25px;
    border-radius: 16px;
    box-shadow: 0px 12px 30px rgba(0,0,0,0.25);
    margin-bottom: 20px;
}}

.result-card {{
    background: linear-gradient(135deg, #0ea5e9, #6366f1);
    color: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0px 12px 30px rgba(0,0,0,0.3);
}}

.footer {{
    text-align: center;
    font-size: 0.9rem;
    color: #e5e7eb;
    margin-top: 40px;
}}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #
st.markdown("<div class='main-title'>✈️ Agentic AI Travel Planner</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Plan smarter trips with AI-powered insights</div>", unsafe_allow_html=True)

# ---------------- INPUT CARD ---------------- #


col1, col2 = st.columns(2)
with col1:
    source = st.text_input("🌍 From City", "Bangalore")
with col2:
    destination = st.text_input("📍 To City", "Goa")

days = st.slider("🗓 Number of Days", 1, 15, 3)
budget = st.number_input("💰 Budget (₹)", 5000, 200000, 20000, step=1000)

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- BUTTON ---------------- #
if st.button("🚀 Generate Travel Plan", use_container_width=True):
    with st.spinner("✨ Creating your personalized itinerary..."):
        plan = run_travel_agent_demo(
            source=source,
            destination=destination,
            days=days,
            budget=budget
        )

    st.markdown("<div class='result-card'>", unsafe_allow_html=True)
    st.markdown("### 🧳 Your Travel Plan")
    st.markdown(plan)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FOOTER ---------------- #
st.markdown("""
<div class='footer'>
Samruddhi Varkhade | 2026
</div>
""", unsafe_allow_html=True)

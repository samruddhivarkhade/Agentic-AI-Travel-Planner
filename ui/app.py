import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import streamlit as st
from agent.travel_agent import run_travel_agent_demo

st.set_page_config(
    page_title="Agentic AI Travel Planner",
    page_icon="✈️",
    layout="centered"
)

st.title("✈️ Agentic AI Travel Planner")
st.write("Plan your trip using an AI-powered travel assistant")

# User Inputs
source = st.text_input("From City", "Bangalore")
destination = st.text_input("To City", "Goa")
days = st.number_input("Number of Days", min_value=1, max_value=15, value=3)
budget = st.number_input("Budget (₹)", min_value=5000, max_value=200000, value=20000)

if st.button("Generate Travel Plan 🚀"):
    with st.spinner("Planning your trip..."):
        plan = run_travel_agent_demo(
            source=source,
            destination=destination,
            days=days,
            budget=budget
        )

    st.success("Travel Plan Generated!")

    st.markdown("---")
    st.markdown(plan)

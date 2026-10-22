import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-3.6-flash")

st.set_page_config(page_title="NetSage AI", page_icon="🌐")

st.title("🌐 NetSage AI")
st.subheader("AI-Powered Network Troubleshooting Assistant")

symptom = st.text_input(
    "Enter Symptom",
    placeholder="Hosts in VLAN 30 cannot communicate"
)

show_output = st.text_area(
    "Paste Show Command Output",
    height=250,
    placeholder="Paste show vlan brief, show interfaces trunk, show ip route output..."
)

if st.button("Diagnose Issue"):

    if symptom and show_output:

        prompt = f"""
You are NetSage AI, a Cisco network troubleshooting assistant.

Analyze the network issue.

Symptom:
{symptom}

Show Output:
{show_output}

Return:
1. Root Cause
2. OSI Layer
3. Confidence
4. Evidence
5. Fix Steps
"""

with st.spinner("Analyzing..."):
    try:
        response = model.generate_content(prompt)

        st.success("Diagnosis Complete")
        st.markdown(response.text)

    except Exception as e:
        st.error(
            "Gemini quota exceeded. Please try again later or use a different API key."
        )

    else:
        st.warning("Please enter symptom and show output.")
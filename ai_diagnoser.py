import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

print("API KEY Loaded:", "Yes" if api_key else "No")

# Configure Gemini
genai.configure(api_key=api_key)

# Model
model = genai.GenerativeModel("gemini-3.6-flash")

# Load dataset
df = pd.read_excel("data/cases.csv.xlsx")

# Test only first 5 cases
df = df.head(5)

correct = 0
total = len(df)

print(f"\nTesting {total} cases...\n")

for index, row in df.iterrows():

    symptom = str(row["Symptom"])
    show_output = str(row["Show_Output"])
    expected_fault = str(row["Expected_Fault"])

    prompt = f"""
You are NetSage AI, a Cisco network troubleshooting assistant.

Analyze the network issue.

Symptom:
{symptom}

Show Output:
{show_output}

Return EXACTLY ONE fault label from the list below.

Fault Labels:
- Missing VLAN
- Wrong VLAN assignment
- Trunk port not configured
- VLAN not allowed on trunk
- Wrong access VLAN
- Interface Down
- Missing Route

Return only the label text and nothing else.
"""

    try:
        response = model.generate_content(prompt)

        ai_diagnosis = response.text.strip()

        print(f"\nCase {index + 1}")
        print("Expected:", expected_fault)
        print("AI:", ai_diagnosis)

        if expected_fault.strip().lower() == ai_diagnosis.strip().lower():
            correct += 1

    except Exception as e:
        print(f"\nCase {index + 1}")
        print("ERROR:", e)

accuracy = (correct / total) * 100

print("\n==============================")
print("FINAL EVALUATION")
print("==============================")
print("Total Cases:", total)
print("Correct Diagnoses:", correct)
print(f"Accuracy: {accuracy:.2f}%")

# NetSage AI - AI-Powered Network Troubleshooting Assistant

NetSage AI is an AI-assisted network troubleshooting system designed to help identify common network configuration problems in Cisco-style lab environments. It combines Python-based rule checking with Google's Gemini API to analyze network symptoms and command outputs and recommend possible root causes and corrective actions.

## Problem Statement

Junior network engineers often struggle to identify the root cause of network connectivity issues. Problems involving VLANs, routing, DHCP, DNS, access control lists, NAT, and wireless configuration can take time to diagnose manually.

NetSage AI aims to simplify this process by analyzing troubleshooting evidence and providing diagnosis recommendations while keeping a human reviewer responsible for approving or correcting the suggested fix.

## Features

- **30-Case Dataset:** Structured troubleshooting cases covering VLAN, routing, DHCP, DNS, ACL, NAT, and wireless issues.
- **Rule-Based Fault Detection:** Python checks for missing VLANs, interfaces that are administratively down, and missing default-route indicators.
- **AI-Powered Diagnosis:** Gemini API integration to analyze symptoms and Cisco command outputs.
- **Troubleshooting Recommendations:** The application can provide a likely root cause, OSI layer, confidence level, supporting evidence, and suggested corrective steps.
- **Interactive Interface:** Streamlit interface for entering network symptoms and command outputs.
- **Human Review Workflow:** Review log for recording whether AI diagnoses are accepted, edited, or rejected.
- **Cisco Packet Tracer:** Simulated network topology and fault scenarios for troubleshooting demonstrations.

## Technologies Used

- Python
- Pandas
- Google Gemini API
- Streamlit
- Cisco Packet Tracer
- Excel
- Visual Studio Code

## Project Structure

```text
NetSage-AI/
├── app.py
├── ai_diagnoser.py
├── checker/
│   └── rule_checker.py
├── data/
│   └── cases.csv.xlsx
├── prompts/
│   └── diagnose_prompt.md
├── logs/
│   └── review_log.xlsx
├── sample_outputs/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

The final Cisco Packet Tracer `.pkt` file can also be included in the project root if it has been saved there.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Sahana2960/Netsage-AI.git
cd Netsage-AI
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API Key

Create a `.env` file in the project root:

```text
GOOGLE_API_KEY=your_gemini_api_key_here
```

Replace the placeholder with your own API key.

**Security:** Never commit the `.env` file or publish your API key. The file should be excluded through `.gitignore`.

### 5. Run the Streamlit Application

From the project root, execute:

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal.

Enter a network symptom, paste the relevant Cisco show-command output, and click the diagnosis button to request AI analysis.

### 6. Run the Rule Checker

Open a separate terminal and execute:

```powershell
cd checker
python rule_checker.py
```

The script runs the rule checks implemented in the project and displays their diagnostic results.

## Example Troubleshooting Scenarios

| Scenario | Diagnostic Evidence |
|---|---|
| Missing VLAN | `show vlan brief` |
| Wrong VLAN assignment | `show vlan brief` |
| Trunk port misconfiguration | `show interfaces trunk` |
| Interface administratively down | `show interfaces status` |
| Missing route | `show ip route` |

Other dataset categories include DHCP, DNS, ACL, NAT, and wireless troubleshooting.

## Human Review and Responsible AI

AI-generated diagnoses are recommendations and must not be treated as automatically verified fixes.

A human reviewer should examine the command-output evidence, verify the suggested cause, and record the decision as Accepted, Edited, or Rejected. Corrections should be documented with an explanation of why the original AI diagnosis was inaccurate or incomplete.

## Limitations

- The rule checker currently uses basic deterministic checks and does not cover every possible network misconfiguration.
- AI diagnosis depends on the quality of the provided symptoms and command outputs.
- Gemini API usage is subject to the applicable model quota and rate limits.
- Network configuration changes should be verified by a human before being applied.

## Future Enhancements

- Expand deterministic checks to cover duplicate IP addresses, subnet-mask errors, gateway mismatches, missing VLANs, interface failures, and routing problems.
- Automate AI-versus-human evaluation and dashboard reporting.
- Improve structured JSON output and evidence-grounded diagnosis.
- Deploy the application for access through a public demo link.

## Conclusion

NetSage AI demonstrates how rule-based validation and generative AI can be combined to assist with network troubleshooting. By analyzing symptoms and command outputs, the system aims to help learners and junior network engineers identify likely faults, investigate supporting evidence, and make better-informed troubleshooting decisions.
<img width="1763" height="805" alt="image" src="https://github.com/user-attachments/assets/8a92b071-bb29-4d41-baf6-eafc93e0b529" />

<img width="1763" height="805" alt="image" src="https://github.com/user-attachments/assets/5a217607-8f60-45b5-abf8-eadd0ffb01b1" />

<img width="1763" height="805" alt="image" src="https://github.com/user-attachments/assets/c3137f6f-4a2a-4256-ab58-26c136630c22" />

<img width="1763" height="805" alt="image" src="https://github.com/user-attachments/assets/ff806cb5-63d3-4777-b513-804796055802" />





# Threat Intelligence Aggregator Dashboard

The Threat Intelligence Aggregator Dashboard is a Python-based application that collects, analyzes, and visualizes threat data from multiple public sources.
It helps cybersecurity analysts identify malicious IPs, and malware indicators in real time.
Built for SOC and threat intel teams, this project simplifies manual investigation by providing an easy-to-use dashboard.



## Features

- **Automatic Data Aggregation** — Fetches latest threat data from multiple public intelligence feeds.
- **Flask Backend API** — Centralized Python backend that fetches and aggregates data from multiple sources (AbuseIPDB, VirusTotal, WHOIS).
- **Data Analysis** – Extracts and summarizes malicious IPs, and malware samples.
- **Automated Analysis** — Fetches and visualizes threat intelligence without manual effort
- **Secure API Handling** — Uses `.env` for API key management (not exposed in code)
- **Customizable Framework** — Modular Python structure for easy expansion and integration with SIEM tools



##  Tech Stack

| Component | Technology |
|------------|-------------|
| **Frontend** | Streamlit |
| **Backend** | Flask |
| **Programming Language** | Python 3.x |
| **Data sources** | AbuseIPDB, VirusTotal, WHOIS |
| **Environment** | dotenv for secure key storage |
| **Visualization** | Streamlit Charts, Tables |



## Installation & Setup

### Step 1: Clone this Repository
```bash
git clone https://github.com/Remyamv/Threat-Intelligence-Aggregator-Dashboard.git
cd ti-aggregator
```
### Step 2: Create virtual environment
```nginx
python -m venv .venv
.\.venv\Scripts\activate
```
### Step 3: Install dependencies
```nginx
pip install -r requirements.txt
```
### Step 4: Configure .env

Create a file named `.env` and add:
```ini
notepad .env
ABUSEIPDB_API_KEY=your_api_key_here
VIRUSTOTAL_API_KEY=your_virustotal_key
```
Get your free key from: https://www.abuseipdb.com/register

Get your VirusTotal key

Create an api key and paste it in `.env` file

### Start the Backend API
```arduino
python app.py
```

The Flask API will start locally on http://127.0.0.1:5000.

### Step 5: Launch dashboard
```arduino
streamlit run dashboard.py
```
Then open the local URL displayed in your terminal (usually http://localhost:8501).

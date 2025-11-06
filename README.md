# Threat Intelligence Dashboard

The Threat Intelligence Aggregator Dashboard is a Python-based application that collects, analyzes, and visualizes threat data from multiple public sources.
It helps cybersecurity analysts identify malicious IPs, and malware indicators in real time.
Built for SOC and threat intel teams, this project simplifies manual investigation by providing an easy-to-use dashboard.



## Features

- **Automatic Data Aggregation** — Fetches latest threat data from multiple public intelligence feeds.
- **Data Analysis** – Extracts and summarizes malicious IPs, and malware samples.
- **Automated Analysis** — Fetches and visualizes threat intelligence without manual effort
- **Secure API Handling** — Uses `.env` for API key management (not exposed in code)
- **Customizable Framework** — Modular Python structure for easy expansion and integration with SIEM tools



##  Tech Stack

| Component | Technology |
|------------|-------------|
| **Frontend** | Streamlit |
| **Backend** | Python 3.x |
| **Data sources** | AbuseIPDB, Feodo Tracker, URLHaus |
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
ABUSEIPDB_API_KEY=your_api_key_here
```
Get your free key from: https://www.abuseipdb.com/register
### Step 5: Run the data fetcher
```css
python main.py
```
### Step 6: Analyze threat data
```nginx
python analyze_data.py
```
### Step 7: Launch dashboard
```arduino
streamlit run dashboard.py
```

# Threat Intelligence Dashboard

The Threat Intelligence Aggregator Dashboard is a Python-based application that collects, analyzes, and visualizes threat data from multiple public sources.
It helps cybersecurity analysts identify malicious IPs, URLs, and malware indicators in real time.
Built for SOC and threat intel teams, this project simplifies manual investigation by providing an easy-to-use dashboard.



## Features

- **Automatic Data Aggregation** — Fetches latest threat data from multiple public intelligence feeds.
- **Interactive Dashboard** — Displays URL and IP reputation results using Streamlit
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

###  Clone this Repository
```bash
git clone https://github.com/Remyamv/Threat-Intelligence-Dashboard.git
cd ti-aggregator
```

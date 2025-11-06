# 🧠 SOC Threat Intelligence Dashboard

A real-time dashboard that aggregates threat intelligence from multiple open sources, helping SOC analysts quickly identify, monitor, and analyze emerging cyber threats. Built using **Python**, **Streamlit**, and **VirusTotal API**, this project simplifies threat data visualization and supports proactive security operations.

---

## Features

- **Multi-Source Threat Aggregation** — Collects data from VirusTotal and other APIs (extensible for MISP, AlienVault OTX, etc.)
- **Interactive Dashboard** — Displays URL and IP reputation results using Streamlit
- **Automated Analysis** — Fetches and visualizes threat intelligence without manual effort
- **Secure API Handling** — Uses `.env` for API key management (not exposed in code)
- **Customizable Framework** — Modular Python structure for easy expansion and integration with SIEM tools

---

##  Tech Stack

| Component | Technology |
|------------|-------------|
| **Frontend** | Streamlit |
| **Backend** | Python 3.x |
| **APIs** | VirusTotal API |
| **Environment** | dotenv for secure key storage |
| **Visualization** | Streamlit Charts, Tables |

---

## Installation & Setup

###  Clone this Repository
```bash
git clone https://github.com/Remyamv/Threat-Intelligence-Dashboard.git
cd SOC-Threat

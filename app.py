from flask import Flask, request, jsonify, render_template
import requests
import whois
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")
ABUSEIPDB_API_KEY = os.getenv("ABUSEIPDB_API_KEY")

@app.route("/check", methods=["POST"])
def check_ip():
    ip = request.json.get("ip")
    result = {"ip": ip}

    # === AbuseIPDB ===
    abuse_url = f"https://api.abuseipdb.com/api/v2/check?ipAddress={ip}"
    headers = {"Key": ABUSEIPDB_API_KEY, "Accept": "application/json"}
    abuse_response = requests.get(abuse_url, headers=headers)
    if abuse_response.status_code == 200:
        data = abuse_response.json()["data"]
        result["abuse_score"] = data["abuseConfidenceScore"]
        result["total_reports"] = data["totalReports"]
        result["country"] = data.get("countryCode", "Unknown")

    # === VirusTotal ===
    vt_url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    headers = {"x-apikey": VIRUSTOTAL_API_KEY}
    vt_response = requests.get(vt_url, headers=headers)
    if vt_response.status_code == 200:
        vt_data = vt_response.json()["data"]["attributes"]["last_analysis_stats"]
        result["vt_malicious"] = vt_data["malicious"]
        result["vt_suspicious"] = vt_data["suspicious"]
        result["vt_harmless"] = vt_data["harmless"]

    # === WHOIS ===
    try:
        w = whois.whois(ip)
        result["whois_org"] = w.org
        result["whois_country"] = w.country
    except Exception as e:
        result["whois_org"] = None
        result["whois_country"] = None

    return jsonify(result)

if __name__ == "__main__":
    app.run(port=5000)

import streamlit as st
import requests
from dotenv import load_dotenv
import os
from datetime import datetime


load_dotenv()
API_KEY = os.getenv("ABUSEIPDB_API_KEY")


def check_ip(ip):
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {
        "Accept": "application/json",
        "Key": API_KEY
    }
    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()["data"]
        return {
            "ip": ip,
            "abuseConfidenceScore": data["abuseConfidenceScore"],
            "country": data["countryCode"],
            "totalReports": data["totalReports"],
            "lastReported": data.get("lastReported", "N/A")
        }
    else:
        return {"ip": ip, "error": f"HTTP {response.status_code}"}


if "history" not in st.session_state:
    st.session_state.history = []


st.set_page_config(page_title="Manual IP Reputation Checker", layout="centered")
st.title(" Manual IP Reputation Checker")

ip_input = st.text_input("Enter IP address:")

if ip_input:
    result = check_ip(ip_input)
    
    
    if "error" in result:
        st.error(f"{result['ip']} : {result['error']}")
    else:
        score = result["abuseConfidenceScore"]
       
        if score >= 75:
            color = ":red[HIGH RISK]"
        elif score >= 40:
            color = ":orange[MEDIUM RISK]"
        else:
            color = ":green[LOW RISK]"
        
        st.subheader(f"IP: {result['ip']} ({color})")
        st.write(f"**Abuse Confidence Score:** {score}%")
        st.write(f"**Total Reports:** {result['totalReports']}")
        st.write(f"**Country:** {result['country']}")
        st.write(f"**Last Reported:** {result['lastReported']}")
        
        
        st.session_state.history.append({
            "IP": result["ip"],
            "Score": score,
            "Country": result["country"],
            "Last Reported": result["lastReported"],
            "Checked At": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })


if st.session_state.history:
    st.subheader(" Recently Checked IPs")
    st.table(st.session_state.history[::-1]) 

import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Threat Intelligence Dashboard", layout="wide")
st.title(" Threat Intelligence Dashboard")

if "history" not in st.session_state:
    st.session_state["history"] = []

ip = st.text_input("Enter IP address and press Enter:")

if ip:
    try:
        response = requests.post("http://127.0.0.1:5000/check", json={"ip": ip})
        if response.status_code == 200:
            result = response.json()
            st.session_state["history"].append(result)
        else:
            st.error("Failed to connect to backend API.")
    except Exception as e:
        st.error(f"Connection error: {e}")

if st.session_state["history"]:
    st.markdown("---")
    latest = st.session_state["history"][-1]
    st.subheader(f"Results for **{latest['ip']}**")

    score = latest.get("abuse_score", 0)
    if score >= 75:
        risk_color = "#FF4C4C"
        risk_label = "High Risk"
    elif score >= 40:
        risk_color = "#FFA500"
        risk_label = "Medium Risk"
    else:
        risk_color = "#4CAF50"
        risk_label = "Low Risk"

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div style="background-color:{risk_color}; padding:15px; border-radius:10px;">
            <h4 style="color:white;">AbuseIPDB</h4>
            <p style="color:white;">Score: {score} ({risk_label})<br>
            Country: {latest.get('country', 'Unknown')}<br>
            Total Reports: {latest.get('total_reports', 'N/A')}</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style="background-color:{risk_color}; padding:15px; border-radius:10px;">
            <h4 style="color:white;">VirusTotal</h4>
            <p style="color:white;">
            Malicious: {latest.get('vt_malicious', 'N/A')}<br>
            Suspicious: {latest.get('vt_suspicious', 'N/A')}<br>
            Harmless: {latest.get('vt_harmless', 'N/A')}
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div style="background-color:{risk_color}; padding:15px; border-radius:10px;">
            <h4 style="color:white;">WHOIS</h4>
            <p style="color:white;">
            Org: {latest.get('whois_org', 'N/A')}<br>
            Country: {latest.get('whois_country', 'N/A')}
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader(" Recently Checked IPs")

    df = pd.DataFrame(st.session_state["history"])
    df.rename(columns={
        "ip": "IP Address",
        "abuse_score": "Abuse Score",
        "vt_malicious": "VT Malicious",
        "vt_suspicious": "VT Suspicious",
        "vt_harmless": "VT Harmless",
        "whois_org": "WHOIS Org",
        "whois_country": "WHOIS Country",
        "country": "Country",
        "total_reports": "Total Reports"
    }, inplace=True)

    st.dataframe(df, use_container_width=True, hide_index=True)

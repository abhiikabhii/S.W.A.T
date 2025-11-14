# S.W.A.T

SWAT is an autonomous **AI-IoT stagnant water monitoring & treatment system** designed to detect mosquito-breeding risks and prevent dengue outbreaks.  
It integrates **Arduino-based pH, turbidity, and flow sensors** with lightweight **AI analytics** powered by Python, Cloudflare Workers AI, and a Streamlit dashboard.

---

## 🚀 Features

### 🔍 Real-Time Monitoring  
- Reads **pH**, **turbidity**, and **flow velocity** continuously  
- Sends data to a Python backend (`api.py`)  
- Visualizes trends on the Streamlit dashboard  

### 🧠 AI-Enhanced Risk Detection  
- Fixed thresholds + lightweight AI risk scoring  
- Cloudflare Workers AI analyzes incoming sensor values  
- Computes a **Breeding Risk Score (0–100)**  
- Flags anomalies and highlights unsafe patterns  

### ⚙️ Automated Treatment Logic (Simulated)  
- If pH > 6 → vinegar correction (simulated)  
- If turbidity too high → warning  
- If flow stagnant → pump activation (simulated)  
- All actions displayed in dashboard output  

### 📊 Dashboard  
Interactive **Streamlit UI** that visualizes:
- Live sensor values  
- Historical trends  
- AI-based “Larvae Risk Meter”  
- Automated treatment actions  

---

## 📡 System Architecture

- **Arduino** → reads pH, turbidity, and flow sensors  
- **Python API (`api.py`)** → receives sensor values & sends responses  
- **Cloudflare Worker (`worker_ai.js`)** → computes AI risk index  
- **Streamlit Dashboard (`streamlit_app.py`)** → real-time visualization  

---

## 🧠 AI Components

- **AI Risk Scoring:**  
  Cloudflare Workers AI analyzes pH, turbidity, and flow to assign risk levels  
- **Anomaly Alerts:**  
  Flags unsafe readings based on thresholds + deviation patterns  
- **Trend Interpretation:**  
  Dashboard shows AI-enhanced insights (peaks, dips, danger zones)

---

## 📁 Repository Structure


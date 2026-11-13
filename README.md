# ⚡ Mumbai Smart Energy

### AI-Powered Load Balancing & Fraud Detection System

---

## 🌍 Overview

Mumbai Smart Energy is an intelligent web-based system designed to improve **electricity distribution efficiency** and **detect fraudulent energy usage** using Machine Learning.

The platform combines:

* 🔍 **Fraud Detection (AI-based anomaly detection)**
* ⚡ **Load Balancing Optimization**
* 🗺️ **Grid Risk Visualization Dashboard**
* 🌱 **Renewable Energy Insights**

Built with a focus on **real-world usability**, the system translates complex grid data into **simple, actionable insights** for both users and operators.

---

## 🚀 Key Features

### 🔍 1. Fraud Detection System

Detects abnormal electricity usage patterns using a trained ML model.

* Inputs: voltage, current, power, load demand, etc.
* Outputs:

  * Fraud probability
  * Classification (Fraud / Normal)
  * Confidence score
  * Explanation (why flagged)

👉 Helps identify:

* Meter tampering
* Unusual consumption spikes
* Neighborhood deviation anomalies

---

### ⚡ 2. Smart Load Balancing

Optimizes electricity usage to reduce overload risk.

* Suggests:

  * Load shifting strategies
  * Estimated savings
  * Overload risk level

👉 Designed for **common users** to reduce electricity bills and grid stress.

---

### 🗺️ 3. Grid Risk Dashboard

Interactive map of Mumbai zones using Leaflet.js.

* Visualizes:

  * Risk levels (Low / Medium / High)
  * Zone-wise explanations
  * Smart recommendations

👉 Example:

* High risk → "Shift usage to off-peak hours"
* Low risk → "Normal usage is safe"

---

### 🌱 4. Renewable Energy Dashboard

Displays renewable contribution across zones.

* City-wide average
* Zone-wise comparison
* Visual insights using charts

👉 Helps understand sustainability trends.

---

## 🧠 Machine Learning Models

### Fraud Detection Model

* Algorithm: Random Forest Classifier
* Features:

  * Electrical parameters (current, voltage, power)
  * Behavioral metrics (deviation ratio, spikes)
* Output: Probability-based classification

---

### Blackout Risk Model

* Predicts grid stress based on:

  * Load demand
  * Zone risk factor
  * Usage anomalies

---

## 🛠️ Tech Stack

**Frontend**

* HTML, CSS, Bootstrap
* JavaScript
* Chart.js, Leaflet.js

**Backend**

* Flask (Python)

**Machine Learning**

* Scikit-learn
* Pandas, NumPy
* Joblib (model persistence)

---

## 📂 Project Structure

```
├── app.py
├── Fraud_Detection.py
├── dashboard.py
├── templates/
│   ├── fraud_detection.html
│   ├── load_balancing.html
│   ├── dashboard_map.html
│   ├── renewables.html
├── static/
│   ├── style.css
│   ├── models (.joblib)
│   ├── geojson files
├── fraud_balance/
│   └── syn_fraud.csv
├── load_bal/
│   └── syn_load_bal.csv
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd project-folder
```

### 2. Install dependencies

```bash
pip install flask pandas numpy scikit-learn joblib
```

### 3. Train the models

```bash
python Fraud_Detection.py
python dashboard.py
```

### 4. Run the application

```bash
python app.py
```

### 5. Open in browser

```
http://127.0.0.1:5000
```

---

## 📊 Example Use Cases

* 🏠 Household checking if their bill is abnormal
* ⚡ Grid operators monitoring high-risk zones
* 🏙️ Smart city planning and optimization
* 🌱 Renewable energy tracking

---

## 💡 Innovation Highlights

* Combines **AI + Smart Grid + UX simplicity**
* Converts technical data into **user-friendly insights**
* Includes **explainability (WHY fraud is detected)**
* Real-world inspired simulation of Mumbai grid

---

## 🔮 Future Improvements

* Real-time IoT meter integration
* Deep learning anomaly detection
* Mobile app version
* Live API integration with power providers

---


⚡ *Powering smarter cities, one prediction at a time.*

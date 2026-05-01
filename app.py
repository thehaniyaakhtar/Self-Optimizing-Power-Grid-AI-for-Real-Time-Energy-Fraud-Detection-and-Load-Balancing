# app.py
from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pandas as pd
import numpy as np
import joblib
import os

app = Flask(__name__)
app.secret_key = "mumbai-grid-2025-secure-key"
bcrypt = Bcrypt(app)

# =========================
# DATABASE
# =========================
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///powergrid.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    db.create_all()

# =========================
# LOAD MODEL
# =========================
fraud_model = joblib.load('static/fraud_model_local.joblib')
scaler = joblib.load('static/scaler.joblib')
encoders = joblib.load('static/encoders.joblib')

# =========================
# FEATURES
# =========================
numerical_cols = [
    'voltage_v','current_a','active_power_kw',
    'reactive_power_kvar','load_demand_kwh',
    'occupancy_level','deviation_neighborhood_ratio'
]

categorical_cols = [
    'household_type','appliance_usage_category',
    'broader_zone','locality'
]

ZONES = ['BEST Central', 'Adani West', 'Tata South', 'MSEDCL Suburbs']

# =========================
# FRAUD FUNCTION (UPDATED)
# =========================
def simple_fraud_check(data):

    feature_order = numerical_cols + categorical_cols

    df = pd.DataFrame([{col: data.get(col) for col in feature_order}])

    df = df.fillna({
        'occupancy_level': 2,
        'household_type': 'Apartment',
        'appliance_usage_category': 'Medium',
        'broader_zone': 'Urban',
        'locality': 'Mumbai'
    })

    # Safe encoding
    for col in categorical_cols:
        try:
            df[col] = encoders[col].transform(df[col])
        except:
            df[col] = 0

    # Scale
    df[numerical_cols] = scaler.transform(df[numerical_cols])

    # Predict
    fraud_prob = fraud_model.predict_proba(df)[0][1]

    print("Fraud Probability:", fraud_prob)

    # =========================
    # EXPLANATION SYSTEM
    # =========================
    def generate_explanation(data):
        reasons = []

        if data.get('load_demand_kwh', 0) > 80:
            reasons.append("High energy consumption")

        if data.get('deviation_neighborhood_ratio', 0) > 2:
            reasons.append("Abnormal usage compared to neighborhood")

        if data.get('current_a', 0) > 18:
            reasons.append("Unusually high current flow")

        if data.get('active_power_kw', 0) > 5:
            reasons.append("High power usage")

        if data.get('load_spike_flag', 0) == 1:
            reasons.append("Sudden load spike detected")

        if not reasons:
            reasons.append("Usage within normal range")

        return reasons

    explanation = generate_explanation(data)

    return {
        "fraud_prob": round(float(fraud_prob), 3),
        "label": "Fraud Detected" if fraud_prob > 0.4 else "Normal Usage",
        "confidence": round(0.6 + abs(fraud_prob - 0.5), 2),
        "explanation": explanation
    }

# =========================
# LOAD BALANCING (UNCHANGED)
# =========================
def optimize_for_home(params):
    load = params.get('load_demand_kwh', 35)
    action = -0.25 if load > 40 else 0.15
    
    return {
        "Suggested_Action": round(action, 2),
        "Adjusted_Load_kWh": round(load + action * 10, 1),
        "Saving_Estimate_Rs": round(max(0, (load - 30) * 4.5), 0),
        "Recommendation": "Shift AC/Geyser to after 10 PM" if load > 40 else "Good timing! Keep it up.",
        "Overload_Risk": "High" if load > 45 else "Low"
    }

# =========================
# ROUTES
# =========================
@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')

# ✅ UPDATED FRAUD ROUTE
@app.route('/fraud-detection', methods=['GET', 'POST'])
def fraud_detection():
    if request.method == 'POST':
        data = request.get_json()
        result = simple_fraud_check(data)

        return jsonify({
            "status": "success",
            "fraud_prob": result["fraud_prob"],
            "label": result["label"],
            "confidence": result["confidence"],
            "explanation": result["explanation"]
        })

    return render_template('fraud_detection.html')

@app.route('/load-balancing', methods=['GET', 'POST'])
def load_balancing():
    if request.method == 'POST':
        data = request.get_json()
        result = optimize_for_home(data)
        return jsonify(result)
    return render_template('load_balancing.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard_map.html')

@app.route('/renewables')
def renewables():
    try:
        df = pd.read_csv('load_bal/syn_load_bal.csv')
        if 'region' not in df.columns:
            df['region'] = [ZONES[i % 4] for i in range(len(df))]
        
        zone_means = df.groupby('region')['renewable_contribution_percent'].mean().round(1).tolist()
        global_avg = round(df['renewable_contribution_percent'].mean(), 1)
    except:
        zone_means = [18.5, 24.1, 19.8, 14.2]
        global_avg = 19.2

    return render_template('renewables.html', 
                         zone_labels=ZONES,
                         zone_values=zone_means,
                         global_avg=global_avg)

@app.route('/renewables-data')
def renewables_data():
    try:
        df = pd.read_csv('load_bal/syn_load_bal.csv')

        if 'region' not in df.columns:
            zones = ['BEST Central', 'Adani West', 'Tata South', 'MSEDCL Suburbs']
            df['region'] = [zones[i % 4] for i in range(len(df))]

        zone_means = df.groupby('region')['renewable_contribution_percent'].mean().round(2).to_dict()

        return {
            "status": "success",
            "zone_means": zone_means,
            "global_avg": float(df['renewable_contribution_percent'].mean())
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}
    
@app.route('/forecast')
def forecast():
    try:
        df = pd.read_csv('load_bal/syn_load_bal.csv')
        predictions = (df.tail(24)['load_demand_kwh'] / 80).round(3).tolist()
    except:
        predictions = [0.45] * 24
    return render_template('forecast.html', predictions=predictions)

@app.route('/alerts')
def alerts():
    alerts = [
        {"zone": "MSEDCL Suburbs", "risk": "High", "message": "High chance of load shedding tonight", "time": "Just now"},
        {"zone": "Adani West", "risk": "Medium", "message": "Peak load time - shift heavy appliances", "time": "1 hour ago"},
    ]
    return render_template('alerts.html', alerts=alerts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = "User"
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route('/professional')
def professional():
    return render_template('professional.html')

@app.route('/fraud-detection-pro')
def fraud_detection_pro():
    return render_template('fraud_detection_pro.html')

@app.route('/load-balancing-pro')
def load_balancing_pro():
    return render_template('load_balancing_pro.html')

# =========================
# RUN
# =========================
if __name__ == "__main__":
    print("🚀 Mumbai Smart Energy App Running...")
    app.run(debug=True, host='0.0.0.0', port=5000)
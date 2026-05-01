# 🌐 Self-Optimizing Power Grid  
**AI for Real-Time Energy Fraud Detection & Load Balancing**

---

## 🚀 Overview  

Urban power grids today face two major challenges:  

- ⚡ Electricity theft (non-technical losses)  
- 🔄 Inefficient load distribution leading to transformer overloads  

This project introduces a **self-optimizing smart grid framework** that combines **Machine Learning (ML)** and **Reinforcement Learning (RL)** into a unified system.  

Unlike traditional approaches, this system forms a **closed-loop pipeline**, enabling real-time, intelligent decision-making.  

---

## 🧠 Key Idea  

**Fraud Detection → Load Balancing Optimization**

- ML detects suspicious consumption patterns  
- Outputs a fraud probability score  
- RL uses this score to make smarter load distribution decisions  

**Outcome:**  
- Reliable demand estimation  
- Reduced overload risk  
- Adaptive grid control  

---

## ⚙️ System Architecture  

### 1. Data Layer  
- Synthetic smart meter data using **Gaussian Copula**  
- Preserves:
  - Feature distributions  
  - Real-world correlations  

---

### 2. Fraud Detection (ML)  
- Model: Logistic Regression (Vertex AI AutoML)  
- Output: Fraud probability (0–1)  

**Evaluation Metrics:**  
- Precision  
- Recall  
- F1-score  
- ROC-AUC  
- PR-AUC  

---

### 3. Load Balancing (RL)  
- Algorithm: Proximal Policy Optimization (PPO)  
- Environment: Custom Gym-based simulation  

**Objectives:**  
- Prevent transformer overload  
- Maintain grid stability  
- Optimize renewable usage  

---

### 4. Integration Layer  

Fraud-aware demand adjustment:
L_effective = L × (1 − f)


- Reduces influence of suspicious consumption  
- Enables risk-aware RL decisions  

---

### 5. Interface  
- Flask-based web application  

**Features:**  
- Real-time monitoring dashboard  
- Fraud detection visualization  
- Load balancing simulation  
- Risk map visualization

---

## 📊 Results  

### Fraud Detection  
- Accuracy ≈ **79.9%**  
- Stable across thresholds  
- Strong precision-recall balance  

---

## 🛠️ Tech Stack  

### Languages & Frameworks  
- Python  
- Flask  

### ML & AI  
- Scikit-learn  
- TensorFlow / PyTorch  
- Stable-Baselines3 (PPO)  

### Data & Cloud  
- Google BigQuery  
- Vertex AI  

### Data Generation  
- Gaussian Copula  
- SDV  

### Visualization  
- Matplotlib  
- Dashboard UI  

---

## 💡 Key Innovations  

- Fraud detection used as a real-time control signal  
- Integration of ML + RL in a closed-loop system  
- Synthetic data with preserved correlations  
- Scalable architecture for urban smart grids  

---

## ⚠️ Limitations  

- Based on synthetic data  
- Single-agent RL (limited scalability)  
- Not yet validated on real-world deployment  

---

## 🎯 Conclusion  

This project demonstrates how AI can transform traditional power grids into intelligent, adaptive, and self-optimizing systems, addressing both efficiency and security in modern urban environments.

---

## 📸 Screenshots

<div align="center">

  <p><strong>Home Dashboard</strong></p>
  <img src="https://github.com/user-attachments/assets/4c53ba13-e368-4627-ac09-862d7384449b" width="85%"/>
  <br><br>

  <p><strong>Home Dashboard 2</strong></p>
  <img src="https://github.com/user-attachments/assets/8799f81c-d922-4e8b-a583-5d18afe39d0e" width="85%"/>
  <br><br>

  <p><strong>Fraud Detection Results</strong></p>
  <img src="https://github.com/user-attachments/assets/eb67160a-7c94-4a2e-8788-b93a7de394c3" width="85%"/>
  <br><br>

  <p><strong>Load Balancing Visualization</strong></p>
  <img src="https://github.com/user-attachments/assets/7b61f547-e2be-4cda-8444-b7e437cb479c" width="85%"/>
  <br><br>

  <p><strong>Performance Metrics</strong></p>
  <img src="https://github.com/user-attachments/assets/140150fe-2fbf-4820-895e-39d30fa83f31" width="85%"/>
  <br><br>

  <p><strong>Renewable Energy Contribution Metrics</strong></p>
  <img src="https://github.com/user-attachments/assets/4d7a10e8-d38c-41c2-b423-0d726104e2b8" width="85%"/>
  <br><br>

  <p><strong>Control Panel</strong></p>
  <img src="https://github.com/user-attachments/assets/906875d6-f08c-4302-a236-77dc754db5fc" width="85%"/>
  <br><br>

  <p><strong>Detailed Analytics View</strong></p>
  <img src="https://github.com/user-attachments/assets/401753f1-4e15-42e6-b4e8-bb89de91a93e" width="85%"/>

</div>


# 📊 RetailPulse – AI-Powered Customer Analytics & Demand Forecasting Platform

> **End-to-End Data Science & Analytics Solution for Retail Demand Prediction & Customer Insights**

![RetailPulse Banner](https://img.shields.io/badge/Version-2.0--Industry--Edition-blueviolet?style=for-the-badge&logo=rocket)
![Status](https://img.shields.io/badge/Status-Production--Ready-success?style=for-the-badge&logo=checkmarx)
![Author](https://img.shields.io/badge/Author-Safae%20ERAJI-indigo?style=for-the-badge&logo=person)
![Supervision](https://img.shields.io/badge/Supervision-Zidio%20Development-blue?style=for-the-badge&logo=shield)
![License](https://img.shields.io/badge/License-Enterprise-orange?style=for-the-badge)

> **Developed by Safae ERAJI under the supervision of Zidio Development**

## 📖 Executive Summary

> [!IMPORTANT]
> **Retailers lose billions annually** due to poor demand forecasting and stock mismanagement. RetailPulse bridges this gap with industrial-grade AI.

### 🛑 The Problem
Fragmented data and legacy forecasting methods lead to costly **overstocking** or **revenue loss** from frequent stockouts.

### ✅ The Solution
**RetailPulse** is a state-of-the-art Analytics platform that leverages:
*   🟢 **Demand Forecasting** (Prophet + LSTM)
*   🔵 **Behavioral Segmentation** (RFM + K-Means)
*   🔴 **Churn Intelligence** (XGBoost + SHAP)
*   🟡 **Inventory Optimization** (ROP/EOQ)

### 🎯 Strategic Goals
*   **Reduce Stockouts by 30–50%** via AI-driven weekly horizons.
*   **Increase Revenue by 15–25%** via optimized inventory turn.
*   **Improve Retention** by neutralizing churn risks in real-time.

---

## 📈 Performance Scorecard

| Metric | Target | Status | Impact |
|:---|:---|:---|:---|
| **Forecast Accuracy** | `MAPE ≤ 12%` | ![High](https://img.shields.io/badge/-High-success) | Precision 30-day horizons |
| **Churn Detection** | `AUC ≥ 0.88` | ![Stable](https://img.shields.io/badge/-Stable-blue) | Early risk identification |
| **Data Throughput** | `10M+ Tx/Mo` | ![Scalable](https://img.shields.io/badge/-Scalable-indigo) | Enterprise-level capacity |
| **Latency** | `< 500ms` | ![Fast](https://img.shields.io/badge/-Fast-orange) | Real-time interactivity |
=======
> “Retailers lose billions due to poor demand forecasting and stock mismanagement. RetailPulse uses advanced analytics and machine learning to predict demand, segment customers, detect churn, and optimize inventory — helping retailers reduce stockouts by 30–50% and increase revenue by 15–25%.”

---

## 🎯 Mission & Why This Project Matters
**Mission**: Build an end-to-end data science platform that ingests sales, customer, and inventory data to deliver accurate demand forecasts, customer segmentation, churn prediction, and inventory optimization recommendations for retail businesses.

**Value for Zidio Development**: Retail clients need data-driven decisions to reduce waste and maximize profit. RetailPulse provides a complete analytics solution that Zidio can offer to supermarket chains, fashion retailers, and ecommerce companies.

---

## 📖 Executive Summary

> **🛑 THE PROBLEM**  
> **Retailers lose billions annually** due to poor demand forecasting and stock mismanagement. Fragmented data and legacy forecasting methods lead to costly **overstocking** or **revenue loss** from frequent stockouts. RetailPulse bridges this gap with industrial-grade AI.

> **✅ THE SOLUTION**  
> **RetailPulse** is a state-of-the-art Analytics platform that leverages:
> 
> *   🟢 **Demand Forecasting** (Prophet + LSTM)
> *   🔵 **Behavioral Segmentation** (RFM + K-Means)
> *   🔴 **Churn Intelligence** (XGBoost + SHAP)
> *   🟡 **Inventory Optimization** (ROP/EOQ)

### 🎯 Strategic Goals & Business Impact
*   **Reduce Stockouts by 30–50%** via AI-driven accurate demand forecasting.
*   **Increase Revenue by 15–25%** through better inventory decisions.
*   **Improve Customer Retention** by identifying at-risk customers early.
*   **Process 10M+ Transactions** per month with daily batch jobs under 5 minutes.

---

## 📈 Performance Scorecard & Non-Functional Requirements

| Metric | Target / Requirement | Status | Business Impact |
|:---|:---|:---|:---|
| **Forecast Accuracy** | `MAPE ≤ 12%` | ![High](https://img.shields.io/badge/-High-success) | Precision 30-day horizons |
| **Churn Detection** | `AUC-ROC ≥ 0.88` (Precision@top20% ≥ 0.75) | ![Stable](https://img.shields.io/badge/-Stable-blue) | Early risk identification |
| **Data Throughput** | `10M+ Tx/Mo` | ![Scalable](https://img.shields.io/badge/-Scalable-indigo) | Enterprise-level capacity |
| **Processing Time** | `< 5 minutes` for daily batch jobs | ![Fast](https://img.shields.io/badge/-Fast-orange) | Real-time interactivity |
| **Observability** | Full MLflow tracking & drift detection | ![Active](https://img.shields.io/badge/-Active-success) | Production MLOps readiness |

---

## 🏗️ Architecture & MLOps Lifecycle

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                       RETAILPULSE v2.0 - MLOps LIFECYCLE                    │
└─────────────────────────────────────────────────────────────────────────────┘

 [ 📦 DATA ENGINEERING ]          [ 🧠 MODEL INTELLIGENCE ]      [ 🛡️ BUSINESS INSIGHTS ]
 ──────────────────────           ─────────────────────────      ───────────────────────
                                             │                              │
 ┌───────────────────┐             ┌───────────────────┐          ┌───────────────────┐
 │ Raw Data Sources  │             │  Analysis Engine  │          │    Interactive    │
 │ (CSV/XLSX/SQL)    │             │  (Feature Engine) │          │     Dashboard     │
 └─────────┬─────────┘             └─────────┬─────────┘          └─────────┬─────────┘
           │                                 │                              │
           ▼                                 ▼                              ▼
 ┌───────────────────┐             ┌───────────────────┐          ┌───────────────────┐
 │  AI Data Mapper   │────────────▶│ RFM / Forecasting │◀─────────┤ Drift Monitoring  │
 │ (Auto-Sanitize)   │             │   Churn / Risk    │          │  (Evidently AI)   │
 └───────────────────┘             └───────────────────┘          └─────────┬─────────┘
                                                                            │
      ▲                                                                     │
      └──────────────────────────[ RETRAINING LOOP ]────────────────────────┘
```

---

## 🛠️ Production Technology Stack

| Category | Technology | Rationale |
|:---|:---|:---|
| **Engine** | ![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white) | Core Logic |
| **Analytics** | ![Pandas](https://img.shields.io/badge/Pandas-2.0-150458?logo=pandas&logoColor=white) ![Sklearn](https://img.shields.io/badge/Scikit--Learn-F7931E?logo=scikit-learn&logoColor=white) | Data Pipeline |
| **Models** | ![Prophet](https://img.shields.io/badge/Facebook--Prophet-008080?logo=facebook&logoColor=white) ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=white) | Hybrid AI |
| **MLOps** | ![MLflow](https://img.shields.io/badge/MLflow-0194E2?logo=mlflow&logoColor=white) ![Evidently](https://img.shields.io/badge/Evidently--AI-6D4AFF) | Observability |
| **App** | ![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white) ![Tailwind](https://img.shields.io/badge/Tailwind--CSS-06B6D4?logo=tailwind-css&logoColor=white) | Frontend |
| **Ops** | ![Airflow](https://img.shields.io/badge/Apache--Airflow-017CEE?logo=apache-airflow&logoColor=white) | Scaling |
| **Language** | ![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white) | Core Logic |
| **Data Processing** | ![Pandas](https://img.shields.io/badge/Pandas-2.0-150458?logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-1.24-013243?logo=numpy&logoColor=white) ![Sklearn](https://img.shields.io/badge/Scikit--Learn-F7931E?logo=scikit-learn&logoColor=white) | Data Pipeline |
| **Forecasting** | ![Prophet](https://img.shields.io/badge/Facebook--Prophet-008080?logo=facebook&logoColor=white) ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=white) | Hybrid AI (Prophet + LSTM) |
| **MLOps** | ![MLflow](https://img.shields.io/badge/MLflow-0194E2?logo=mlflow&logoColor=white) ![Evidently](https://img.shields.io/badge/Evidently--AI-6D4AFF) | Experiment tracking & Drift detection |
| **App / Dashboard** | ![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white) | Frontend & Visualizations |
| **Database** | PostgreSQL + Redis | Structured data + caching |
| **Orchestration** | ![Airflow](https://img.shields.io/badge/Apache--Airflow-017CEE?logo=apache-airflow&logoColor=white) | Scalable production deployment |
| **Monitoring** | Prometheus + Grafana | Performance monitoring |


---

## 📅 Execution Timeline

> [!TIP]
> **Agile Delivery**: This project followed a rigorous 28-day sprint cycle.

*   🗓️ **Week 1**: **Exploration & Baseline** — EDA, data cleaning, and Prophet integration.
*   🗓️ **Week 2**: **Advanced Modeling** — LSTM Ensembles, XGBoost, and Optuna tuning.
*   🗓️ **Week 3**: **Deployment** — Flask dashboard development and RBAC setup.
*   🗓️ **Week 4**: **Production** — MLOps integration (MLflow/Evidently) and QA.

---

## 🛡️ Security & Reliability

*   🔒 **Data Privacy**: Automated anonymization of PII during ingestion.
*   🚦 **RBAC**: Segmented views for **Executive**, **Marketing**, and **Inventory** roles.
*   ⚡ **Scalability**: Designed to process **10M+ transactions** per month.
*   📡 **Monitoring**: Real-time drift detection via **Evidently AI**.

---

## 🚀 Live Deployment
RetailPulse is deployed and accessible online via **Render** — no local setup needed to view the dashboard.

| Detail | Value |
|:---|:---|
| **Platform** | [Render](https://render.com) |
| **Live URL** | [retailpulse-sd7y.onrender.com](https://retailpulse-sd7y.onrender.com) |
| **Auto-Deploy** | ✅ Enabled — every push to `main` triggers a live update |
| **SSL/HTTPS** | ✅ Enforced automatically |
| **Stack** | Flask + Gunicorn |

> [!NOTE]
> The free Render instance spins down after 15 minutes of inactivity. The first visit may take 30–50 seconds to wake up. Upgrade to a paid plan for instant response.

---

## 💭 Reflection & Roadmap
> **Note:** The free Render instance spins down after 15 minutes of inactivity. The first visit may take 30–50 seconds to wake up. Upgrade to a paid plan for instant response.

---

## 🛡️ Security & Privacy Highlights
*   **Data Privacy**: Automated anonymization of PII during ingestion.
*   **RBAC**: Segmented views for Executive, Marketing, and Inventory roles.
*   **Secure API endpoints** with JWT.
*   **Audit logging** for sensitive operations.

---

## 💡 Challenges, Learnings & Industry Best Practices
*   **Handling non-stationary time-series data** with proper decomposition.
*   **Balancing model accuracy with interpretability** using SHAP.
*   **Best practices**: MLflow for reproducibility, Evidently AI for drift detection, Airflow for orchestration.

### 💭 Reflection & Roadmap
**Key Learnings**: Transitioning from static models to a dynamic MLOps pipeline using MLflow was the most impactful shift.

**Future Roadmap**:
1.  🏃 **Real-time Streaming**: Kafka-based ingestion for instant stock updates.
2.  🌐 **Global Localization**: Multi-currency and multi-language support.

---


## ⚙️ Easy Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Safae26/RetailPulse.git
   cd RetailPulse
   ```
2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Flask Dashboard:**
   ```bash
   python app/app.py
   ```
5. **Access the application:** Open `http://localhost:5000` in your web browser.

---

> **Done by Safae ERAJI under the supervision of Zidio Development** • March 2026  
> **Submitted for:** Data Science & Analytics Domain
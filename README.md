# 📊 RetailPulse – AI-Powered Customer Analytics & Demand Forecasting Platform

> **End-to-End Data Science & Analytics Solution for Retail Demand Prediction & Customer Insights**

![RetailPulse Banner](https://img.shields.io/badge/Version-2.0--Industry--Edition-blueviolet?style=for-the-badge&logo=rocket)
![Status](https://img.shields.io/badge/Status-Production--Ready-success?style=for-the-badge&logo=checkmarx)
![Author](https://img.shields.io/badge/Author-Safae%20ERAJI-indigo?style=for-the-badge&logo=person)
![Supervision](https://img.shields.io/badge/Supervision-Zidio%20Development-blue?style=for-the-badge&logo=shield)
![License](https://img.shields.io/badge/License-Enterprise-orange?style=for-the-badge)

> “Retailers lose billions due to poor demand forecasting and stock mismanagement. RetailPulse uses advanced analytics and machine learning to predict demand, segment customers, detect churn, and optimize inventory — helping retailers reduce stockouts by 30–50% and increase revenue by 15–25%.”

---

## 🎯 Mission
Build an end-to-end data science platform that ingests sales, customer, and inventory data to deliver accurate demand forecasts, customer segmentation, churn prediction, and inventory optimization recommendations for retail businesses.

## 🏢 Why This Project Matters for Zidio Development
Retail clients need data-driven decisions to reduce waste and maximize profit. RetailPulse provides a complete analytics solution that Zidio can offer to supermarket chains, fashion retailers, and ecommerce companies.

## 📈 Quantified Business Impact Targets
*   **Reduce stockouts by 30–50%** through accurate demand forecasting.
*   **Increase revenue by 15–25%** through better inventory decisions.
*   **Improve customer retention** by identifying at-risk customers early.
*   **Process 10M+ transactions** per month with daily batch jobs under 5 minutes.

## ⚡ Non-Functional Requirements
*   **Model accuracy**: MAPE ≤ 12% for demand forecasting.
*   **Processing time**: < 5 minutes for daily batch jobs.
*   **Scalability**: Handle 10M+ transactions per month.
*   **Observability**: Full MLflow tracking and drift detection.

---

## 🧠 Core MLOps Pipeline & Architecture

*(Insert Screenshot / Excalidraw Diagram Here)*

1.  **Data Ingestion & Cleaning**: Ingest sales, customer, and inventory data from multiple sources (Automated ETL pipeline, data quality checks).
2.  **Customer Segmentation**: RFM + behavioral segmentation using K-Means / DBSCAN. 8 meaningful segments with business interpretation.
3.  **Demand Forecasting**: Time-series forecasting with Prophet + LSTM ensemble. MAPE ≤ 12%, 30-day ahead predictions.
4.  **Churn Prediction**: Classification model to identify at-risk customers. AUC-ROC ≥ 0.88, precision@top20% ≥ 0.75.
5.  **Inventory Optimization**: Recommend reorder quantities using forecasted demand. Reduce overstock/understock by 25–40%.
6.  **Interactive Analytics Flask Dashboard**: Real-time insights, exportable reports, visualizations, and what-if analysis.

---

## 🛠️ Production Technology Stack
*   **Language**: Python 3.11
*   **Data Processing**: Pandas, NumPy, Scikit-learn
*   **Time-series Forecasting**: Prophet + LSTM (PyTorch)
*   **Dashboard**: Flask
*   **Experiment Tracking**: MLflow (Model versioning and reproducibility)
*   **Database**: PostgreSQL + Redis (Structured data + caching)
*   **Containerization**: Docker (Consistent deployment)
*   **Orchestration**: Kubernetes (Scalable production deployment)
*   **Monitoring**: Prometheus + Grafana + EvidentlyAI (Drift detection)

---

## 📅 Execution Timeline

### Week 1 – Data Exploration & Preparation
*   Dataset selection (retail sales, customer, inventory data)
*   Initial EDA notebook: distribution analysis, missing values, correlation heatmap
*   Data cleaning and feature engineering (RFM scores, rolling statistics)
*   Data validation with Great Expectations
*   Customer segmentation using K-Means and DBSCAN
*   Cluster evaluation and business interpretation
*   Time-series data preparation for forecasting
*   Stationarity tests and decomposition
*   Baseline Prophet model for demand forecasting
*   LSTM model implementation with PyTorch Lightning
*   **Checkpoint**: EDA report, cleaned dataset, baseline models logged in MLflow

### Week 2 – Advanced Modeling & Churn Prediction
*   Hybrid forecasting model (Prophet + LSTM ensemble)
*   Churn prediction model using XGBoost with SHAP explainability
*   Inventory optimization logic using forecasted demand
*   Feature importance analysis and model tuning with Optuna
*   Drift detection setup using Evidently AI
*   Automated retraining pipeline with Airflow
*   **Checkpoint**: Forecasting and churn models ready, optimization logic implemented

### Week 3 – Dashboard & Analytics Layer
*   Flask dashboard skeleton with multi-page layout
*   Demand forecasting visualizations and what-if analysis
*   Customer segmentation and churn risk dashboard
*   Inventory optimization recommendations UI
*   Real-time metrics and alerts
*   Export functionality (CSV/PDF reports)
*   **Checkpoint**: Fully interactive dashboard with all insights

### Week 4 – Deployment & Production Polish
*   Docker multi-stage builds for the application
*   Kubernetes manifests and deployment configuration
*   GitHub Actions CI/CD pipeline
*   Cloud deployment on AWS or GCP
*   Monitoring setup with Prometheus and Grafana
*   Load testing and final accuracy validation
*   Final QA, README polishing, demo video recording, PDF export

---

## 🚀 Live Deployment
RetailPulse is configured for scalable cloud deployment via **AWS / GCP**. 
*(Note: This application is not hosted on Render for production).*

### 🔗 Public Demo URL
Soon

### 📺 Demo Video
Soon

### 🖼️ Platform Showcase
Soon

---

## 🛡️ Security & Privacy Highlights
*   **Data anonymization** for customer records.
*   **Role-based access** in the dashboard.
*   **Secure API endpoints** with JWT.
*   **Audit logging** for sensitive operations.

---

## 💡 Challenges, Learnings & Industry Best Practices
*   **Handling non-stationary time-series data** with proper decomposition.
*   **Balancing model accuracy with interpretability** using SHAP.
*   **Best practices**: MLflow for reproducibility, Evidently AI for drift detection, Airflow for orchestration.

### Personal Growth Reflection
*(Insert personal reflection here detailing technical maturity gained through MLOps, deployment, and end-to-end data science lifecycle management.)*

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

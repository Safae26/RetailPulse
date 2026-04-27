"""
RetailPulse Automated Retraining Pipeline
=========================================
Runs monthly to:
1. Ingest latest transaction data
2. Recompute RFM features + churn labels
3. Retrain XGBoost model

Deploy: Copy to Airflow's dags/ folder on a Linux instance.
"""

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
import os
import pathlib
import logging
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

log = logging.getLogger(__name__)

# --- Configuration ---
BASE_DIR = pathlib.Path(__file__).parent.parent  # RetailPulse root
DATA_DIR = BASE_DIR / 'data' / 'processed'
MODEL_DIR = BASE_DIR / 'models'

# --- Pipeline Functions ---

def ingest_data(**kwargs):
    """Load pre-processed transaction data."""
    df = pd.read_csv(DATA_DIR / 'online_retail_initial.csv', parse_dates=['InvoiceDate'])
    log.info(f"Ingested {len(df):,} rows")
    
    # Push file path instead of dataframe (XCom-safe)
    kwargs['ti'].xcom_push(key='data_path', value=str(DATA_DIR / 'online_retail_initial.csv'))
    return len(df)

def feature_engineering(**kwargs):
    """Engineer RFM features and create churn labels."""
    df = pd.read_csv(DATA_DIR / 'online_retail_initial.csv', parse_dates=['InvoiceDate'])
    
    max_date = df['InvoiceDate'].max()
    cutoff_date = max_date - timedelta(days=90)
    
    obs_df = df[df['InvoiceDate'] <= cutoff_date]
    future_df = df[df['InvoiceDate'] > cutoff_date]
    returning_customers = future_df['CustomerID'].dropna().unique()
    
    snapshot_date = obs_df['InvoiceDate'].max() + timedelta(days=1)
    rfm = obs_df.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
        'InvoiceNo': 'nunique',
        'TotalPrice': 'sum'
    }).reset_index()
    rfm.columns = ['CustomerID', 'Recency', 'Frequency', 'Monetary']
    
    # Churn labels
    rfm['Churn'] = rfm['CustomerID'].apply(lambda x: 0 if x in returning_customers else 1)
    
    rfm_path = DATA_DIR / 'rfm_churn_features.csv'
    rfm.to_csv(rfm_path, index=False)
    kwargs['ti'].xcom_push(key='rfm_path', value=str(rfm_path))
    
    churn_rate = rfm['Churn'].mean()
    log.info(f"Features saved. Churn rate: {churn_rate:.1%}")
    return churn_rate

def retrain_model(**kwargs):
    """Retrain XGBoost with latest data."""
    ti = kwargs['ti']
    rfm_path = ti.xcom_pull(key='rfm_path', task_ids='feature_engineering')
    rfm = pd.read_csv(rfm_path)
    
    X = rfm[['Recency', 'Frequency', 'Monetary']]
    y = rfm['Churn']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = XGBClassifier(n_estimators=200, max_depth=4, learning_rate=0.1)
    model.fit(X_train, y_train)
    
    auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])
    log.info(f"Model AUC: {auc:.4f}")
    
    MODEL_DIR.mkdir(exist_ok=True)
    model.save_model(str(MODEL_DIR / 'churn_xgb_model_latest.json'))
    log.info(f"Model saved to {MODEL_DIR}")

# --- DAG Definition ---

default_args = {
    'owner': 'Safae',
    'depends_on_past': False,
    'start_date': datetime(2026, 4, 23),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'retail_pulse_retraining_pipeline',
    default_args=default_args,
    description='🔄 Monthly churn model retraining pipeline',
    schedule=timedelta(days=30),
    catchup=False,
    tags=['retail', 'churn', 'xgboost'],
) as dag:

    task_ingest = PythonOperator(
        task_id='ingest_data',
        python_callable=ingest_data,
    )

    task_features = PythonOperator(
        task_id='feature_engineering',
        python_callable=feature_engineering,
    )

    task_train = PythonOperator(
        task_id='retrain_model',
        python_callable=retrain_model,
    )

    task_ingest >> task_features >> task_train
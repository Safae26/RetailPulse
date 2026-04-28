# RetailPulse Demand Forecasting — historical data, what-if, model metrics

import pandas as pd
import numpy as np
from pathlib import Path
from datetime import timedelta
import json

class DemandForecasting:
    """
    Load weekly revenue and serve historical trends + what-if projections.
    """
    def __init__(self, data_dir=None):
        self.base_dir = Path(__file__).parent.parent.parent
        self.processed_dir = Path(data_dir) if data_dir else (self.base_dir / 'data' / 'processed')
        self.models_dir = self.base_dir / 'models'

        self.weekly = None
        self.monthly = None
        self.prophet_metrics = None
        self.lstm_metrics = None
        self._load_data()

    def reload(self, data_dir):
        """Update source and reload."""
        self.processed_dir = Path(data_dir)
        self._load_data()

    def _load_data(self):
        """Load all time-series data."""
        w_path = self.processed_dir / 'weekly_revenue.csv'
        if w_path.exists():
            try:
                self.weekly = pd.read_csv(w_path, encoding='utf-8')
            except UnicodeDecodeError:
                self.weekly = pd.read_csv(w_path, encoding='latin1')
            
            # Normalize column names for user-uploaded data
            if 'ds' in self.weekly.columns and 'y' in self.weekly.columns:
                self.weekly = self.weekly.rename(columns={'ds': 'Date', 'y': 'TotalPrice'})
            self.weekly['Date'] = pd.to_datetime(self.weekly['Date'])

        m_path = self.processed_dir / 'monthly_revenue.csv'
        if m_path.exists():
            try:
                self.monthly = pd.read_csv(m_path, encoding='utf-8')
            except UnicodeDecodeError:
                self.monthly = pd.read_csv(m_path, encoding='latin1')
                
            if 'ds' in self.monthly.columns and 'y' in self.monthly.columns:
                self.monthly = self.monthly.rename(columns={'ds': 'Date', 'y': 'TotalPrice'})
            self.monthly['Date'] = pd.to_datetime(self.monthly['Date'])

        # Load model metrics
        p_path = self.models_dir / 'prophet_metrics.json'
        if p_path.exists():
            with open(p_path) as f:
                self.prophet_metrics = json.load(f)

        l_path = self.models_dir / 'lstm_metrics.json'
        if l_path.exists():
            with open(l_path) as f:
                self.lstm_metrics = json.load(f)

    # ── Historical Data ──────────────────────────────
    def get_historical(self):
        """Return weekly revenue for Chart.js."""
        if self.weekly is None:
            return [], []
        return (
            self.weekly['Date'].dt.strftime('%Y-%m-%d').tolist(),
            self.weekly['TotalPrice'].round(0).tolist()
        )

    def get_monthly(self):
        """Return monthly revenue for bar chart."""
        if self.monthly is None:
            return [], []
        return (
            self.monthly['Date'].dt.strftime('%Y-%m').tolist(),
            self.monthly['TotalPrice'].round(0).tolist()
        )

    def get_stats(self):
        """Return summary statistics."""
        if self.weekly is None:
            return {}
        return {
            'total_revenue': f"£{self.weekly['TotalPrice'].sum():,.0f}",
            'avg_weekly': f"£{self.weekly['TotalPrice'].mean():,.0f}",
            'peak_week': f"£{self.weekly['TotalPrice'].max():,.0f}",
            'num_weeks': len(self.weekly),
            'date_start': self.weekly['Date'].min().strftime('%Y-%m-%d'),
            'date_end': self.weekly['Date'].max().strftime('%Y-%m-%d'),
        }

    # ── What-If Projection ────────────────────────────
    def get_what_if(self, growth_rate=10, weeks=12):
        """Simple compound growth projection."""
        if self.weekly is None:
            return [], [], []

        last = self.weekly['TotalPrice'].iloc[-1]
        projected = [last * (1 + growth_rate / 100) ** i for i in range(weeks)]
        future_dates = pd.date_range(
            self.weekly['Date'].iloc[-1] + timedelta(days=7),
            periods=weeks, freq='W'
        )

        return (
            future_dates.strftime('%Y-%m-%d').tolist(),
            [round(v, 0) for v in projected],
            round(sum(projected[:12]), 0)
        )

    # ── Model Metrics ─────────────────────────────────
    def get_model_metrics(self):
        """Return Prophet + LSTM MAPE."""
        return {
            'prophet_mape': self.prophet_metrics.get('MAPE', 'N/A') if self.prophet_metrics else 'N/A',
            'lstm_mape': self.lstm_metrics.get('MAPE', 'N/A') if self.lstm_metrics else 'N/A',
        }
# RetailPulse RFM Analysis — loads customer segments, serves summaries & lookups

import pandas as pd
import numpy as np
from pathlib import Path

class RFMAnalysis:
    def __init__(self, data_dir=None):
        self.base_dir = Path(__file__).parent.parent.parent
        self.processed_dir = Path(data_dir) if data_dir else (self.base_dir / 'data' / 'processed')
        self.segments = None
        self.rfm = None
        self._load_data()

    def reload(self, data_dir):
        """Update the data source and reload features."""
        self.processed_dir = Path(data_dir)
        self._load_data()

    def _load_data(self):
        # Load customer segments
        seg_path = self.processed_dir / 'customer_segments.csv'
        if seg_path.exists():
            try:
                self.segments = pd.read_csv(seg_path, encoding='utf-8')
            except UnicodeDecodeError:
                self.segments = pd.read_csv(seg_path, encoding='latin1')

        # Load raw RFM features
        rfm_path = self.processed_dir / 'rfm_features.csv'
        if rfm_path.exists():
            try:
                self.rfm = pd.read_csv(rfm_path, encoding='utf-8')
            except UnicodeDecodeError:
                self.rfm = pd.read_csv(rfm_path, encoding='latin1')

    # ── Segment Summary ──────────────────────────────
    def get_segment_summary(self):
        """Return aggregated segment statistics."""
        if self.segments is None:
            return pd.DataFrame()

        if 'Segment_Name' not in self.segments.columns:
            return self.segments.describe().reset_index()

        summary = self.segments.groupby('Segment_Name').agg(
            Customers=('Recency', 'count'),
            Avg_Recency=('Recency', 'mean'),
            Avg_Frequency=('Frequency', 'mean'),
            Avg_Monetary=('Monetary', 'mean'),
            Total_Revenue=('Monetary', 'sum')
        ).round(1)
        summary = summary.sort_values('Total_Revenue', ascending=False)
        return summary

    def get_segment_distribution(self):
        """Return segment sizes for pie/bar charts."""
        if self.segments is None or 'Segment_Name' not in self.segments.columns:
            return {}
        counts = self.segments['Segment_Name'].value_counts()
        return {'labels': counts.index.tolist(), 'values': counts.values.tolist()}

    def get_rfm_scores(self):
        """Return raw RFM scores for scatter plots."""
        if self.segments is None:
            return []
        cols = ['Recency', 'Frequency', 'Monetary', 'Segment_Name']
        if 'CustomerID' in self.segments.columns:
            cols = ['CustomerID'] + cols
        available = [c for c in cols if c in self.segments.columns]
        return self.segments[available].to_dict('records')

    # ── Customer Lookup ──────────────────────────────
    def get_customer_details(self, customer_id=None, segment=None, limit=100):
        """Return filtered customer records."""
        df = self.segments.copy() if self.segments is not None else pd.DataFrame()
        if df.empty:
            return []

        if customer_id and 'CustomerID' in df.columns:
            df = df[df['CustomerID'].astype(str) == str(customer_id)]
        if segment and 'Segment_Name' in df.columns:
            df = df[df['Segment_Name'] == segment]

        cols = ['Recency', 'Frequency', 'Monetary']
        if 'CustomerID' in df.columns:
            cols = ['CustomerID'] + cols
        if 'Segment_Name' in df.columns:
            cols.append('Segment_Name')

        return df[cols].head(limit).to_dict('records')

    # ── Segment Profiles (static) ────────────────────
    @staticmethod
    def get_segment_profiles():
        return [
            {"name": "Champions", "desc": "Best customers — high spend, frequent, recent",
             "action": "VIP treatment, early access, loyalty perks", "color": "#2ecc71"},
            {"name": "Loyal Customers", "desc": "Regular buyers needing occasional engagement",
             "action": "Upsell, referral programs", "color": "#3498db"},
            {"name": "Potential Loyalists", "desc": "Recent, decent spend, few orders",
             "action": "Nurture with personalized recommendations", "color": "#9b59b6"},
            {"name": "Recent/New Customers", "desc": "Just arrived — 1-2 purchases",
             "action": "Welcome sequence, onboarding", "color": "#1abc9c"},
            {"name": "Promising", "desc": "Recent but low spend",
             "action": "Bundle deals, upsell", "color": "#f39c12"},
            {"name": "Needs Attention", "desc": "Good history, gone quiet",
             "action": "Reactivation campaign", "color": "#e67e22"},
            {"name": "At Risk", "desc": "Big spenders who left",
             "action": "Personal outreach, exclusive offer", "color": "#e74c3c"},
            {"name": "Hibernating / Lost", "desc": "Almost gone",
             "action": "Last-chance discount", "color": "#95a5a6"},
        ]
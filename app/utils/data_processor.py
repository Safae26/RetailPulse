import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.cluster import KMeans

class DataProcessor:
    def __init__(self, output_dir):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def process_csv(self, file_path):
        """Transform raw retail data (CSV or Excel) into standard features."""
        ext = str(file_path).lower().split('.')[-1]
        
        try:
            if ext in ['xlsx', 'xls']:
                df = pd.read_excel(file_path)
            else:
                # use sep=None to auto-detect and on_bad_lines='skip' for resilience
                df = pd.read_csv(file_path, sep=None, engine='python', encoding='utf-8', on_bad_lines='skip')
                # Handle cases where Excel paste might result in single tab-separated column
                if len(df.columns) <= 1:
                    df = pd.read_csv(file_path, sep='\t', encoding='utf-8', on_bad_lines='skip')
        except Exception:
            if ext in ['xlsx', 'xls']:
                raise
            df = pd.read_csv(file_path, sep=None, engine='python', encoding='latin1', on_bad_lines='skip')
            if len(df.columns) <= 1:
                df = pd.read_csv(file_path, sep='\t', encoding='latin1', on_bad_lines='skip')
        
        # 1. Clean Column Names (Strip whitespace and hidden characters)
        df.columns = [str(c).strip() for c in df.columns]
        
        # 2. AI Data Mapper - Normalize common retail column names (Case-Insensitive)
        col_map = {
            'invoicedate': 'Date', 'date': 'Date', 'timestamp': 'Date', 'datetime': 'Date', 'period': 'Date',
            'customerid': 'CustomerID', 'customer id': 'CustomerID', 'customer_id': 'CustomerID', 'userid': 'CustomerID', 'user_id': 'CustomerID', 'client': 'CustomerID',
            'quantity': 'Quantity', 'qty': 'Quantity', 'units': 'Quantity', 'count': 'Quantity',
            'unitprice': 'Price', 'price': 'Price', 'unit price': 'Price', 'unit_price': 'Price', 'amount': 'Price'
        }
        
        # Apply mapping by lowercasing current columns
        current_cols = {c.lower(): c for c in df.columns}
        rename_dict = {}
        for alias, standard in col_map.items():
            if alias in current_cols:
                rename_dict[current_cols[alias]] = standard
        
        df = df.rename(columns=rename_dict)
        
        if 'Date' not in df.columns or 'CustomerID' not in df.columns:
            detected = ", ".join(df.columns)
            raise ValueError(f"Missing required columns. Detected: [{detected}]. Please ensure 'Date' and 'CustomerID' exist.")

        df['Date'] = pd.to_datetime(df['Date'])
        df['Monetary'] = df['Quantity'] * df['Price']
        
        # 2. RFM Features
        latest_date = df['Date'].max()
        rfm = df.groupby('CustomerID').agg({
            'Date': lambda x: (latest_date - x.max()).days,
            'CustomerID': 'count',
            'Monetary': 'sum'
        }).rename(columns={'Date': 'Recency', 'CustomerID': 'Frequency'})
        
        # 3. K-Means Segmentation (Standard 8 clusters for v2)
        kmeans = KMeans(n_clusters=8, random_state=42, n_init=10)
        # Log transform for better clustering
        rfm_log = np.log1p(rfm)
        rfm['Cluster'] = kmeans.fit_predict(rfm_log)
        
        # Map clusters to names (simplified)
        cluster_map = {
            0: 'Champions', 1: 'Loyal Customers', 2: 'Potential Loyalist',
            3: 'Recent Customers', 4: 'Promising', 5: 'At Risk',
            6: 'Needs Attention', 7: 'Hibernating'
        }
        rfm['Segment_Name'] = rfm['Cluster'].map(cluster_map)
        
        # 4. Save Processed Data
        rfm.to_csv(self.output_dir / 'rfm_features.csv')
        rfm.to_csv(self.output_dir / 'customer_segments.csv') # Used by segments.html
        
        # 5. Demand Data (Weekly)
        demand = df.set_index('Date')['Monetary'].resample('W').sum().reset_index()
        demand.columns = ['ds', 'y']
        demand.to_csv(self.output_dir / 'weekly_demand.csv')
        
        return True

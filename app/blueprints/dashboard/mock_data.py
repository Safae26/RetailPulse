import random

def get_mock_data():
    """Return realistic mock data for the dashboard."""
    return {
        'stats': {
            'total_revenue': '£8,245,000',
            'avg_weekly': '£158,500',
            'peak_week': '£245,000',
            'num_weeks': 104,
            'date_start': '2010-01-01',
            'date_end': '2011-12-31',
        },
        'total_customers': 4373,
        'segment_count': 8,
        'churn': {
            'auc_roc': 0.840,
            'churn_rate': '24.0%',
            'model': 'XGBoost (Optuna-tuned)',
        },
        'historical': {
            'dates': [f'2010-W{w:02d}' for w in range(1, 53)] + [f'2011-W{w:02d}' for w in range(1, 53)],
            'values': [random.randint(120000, 220000) for _ in range(104)],
        },
        'segment_distribution': {
            'labels': ['Champions', 'Loyal', 'Potential Loyalists', 'New', 'Promising', 'Needs Attention', 'At Risk', 'Hibernating'],
            'values': [620, 850, 720, 580, 490, 380, 410, 323],
        },
    }
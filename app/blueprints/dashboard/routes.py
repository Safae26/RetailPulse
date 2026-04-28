import os
from flask import render_template, jsonify, request, current_app, session
from . import dashboard_bp
from app.models.rfm_analysis import RFMAnalysis
from app.models.demand_forecasting import DemandForecasting
from app.models.churn_prediction import ChurnPrediction
from app.models.inventory_optimization import InventoryOptimization
from app.utils.data_processor import DataProcessor

# Global Model Instances
rfm_model = RFMAnalysis()
forecast_model = DemandForecasting()
churn_model = ChurnPrediction()
inventory_model = InventoryOptimization()

# Data Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'data', 'uploads')
DEFAULT_DATA_DIR = os.path.join(BASE_DIR, 'data', 'processed')

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
processor = DataProcessor(UPLOAD_FOLDER)

@dashboard_bp.route('/data')
def data_center():
    is_custom = session.get('custom_data', False)
    return render_template('upload.html', is_custom=is_custom)

@dashboard_bp.route('/api/data/upload', methods=['POST'])
def api_upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Empty filename'}), 400

    # Preserve extension
    ext = file.filename.lower().split('.')[-1]
    file_path = os.path.join(UPLOAD_FOLDER, f'raw_upload.{ext}')
    file.save(file_path)
    
    try:
        processor.process_csv(file_path)
        # Shift models to use upload folder
        rfm_model.reload(UPLOAD_FOLDER)
        forecast_model.reload(UPLOAD_FOLDER)
        session['custom_data'] = True
        return jsonify({'success': 'Dataset processed successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@dashboard_bp.route('/api/data/reset', methods=['POST'])
def api_reset():
    rfm_model.reload(DEFAULT_DATA_DIR)
    forecast_model.reload(DEFAULT_DATA_DIR)
    session['custom_data'] = False
    return jsonify({'success': 'Reverted to default dataset'})

@dashboard_bp.route('/')
def index():
    return render_template('index.html')


@dashboard_bp.route('/forecasting')
def forecasting():
    return render_template('forecasting.html')


@dashboard_bp.route('/sales')
def sales():
    return render_template('sales.html')


@dashboard_bp.route('/segments')
def segments():
    return render_template('segments.html')


@dashboard_bp.route('/churn')
def churn():
    return render_template('churn.html')


@dashboard_bp.route('/inventory')
def inventory():
    return render_template('inventory.html')


@dashboard_bp.route('/reports')
def reports():
    return render_template('reports.html')


# ── Overview API ──

@dashboard_bp.route('/api/overview/kpi')
@dashboard_bp.route('/api/dashboard/stats') # Alias for legacy calls
def api_kpi():
    stats = forecast_model.get_stats()
    dist = rfm_model.get_segment_distribution()
    churn_stats = churn_model.get_summary()
    return jsonify({
        'revenue': stats.get('total_revenue', '£0'),
        'customers': sum(dist.get('values', [])),
        'orders': stats.get('num_weeks', 0),
        'churn': churn_stats.get('churn_rate', '0%'),
        'stats': stats, # Extra data just in case
        'total_customers': sum(dist.get('values', [])),
        'segment_count': len(dist.get('labels', [])),
        'churn_data': churn_stats
    })


# ── Forecasting API ──

@dashboard_bp.route('/api/forecast/stats')
def api_forecast_stats():
    return jsonify(forecast_model.get_stats())


@dashboard_bp.route('/api/forecast/historical')
def api_forecast_historical():
    dates, values = forecast_model.get_historical()
    return jsonify({'dates': dates, 'values': values})


@dashboard_bp.route('/api/forecast/what-if')
def api_forecast_what_if():
    growth = float(request.args.get('growth', 10))
    weeks = int(request.args.get('weeks', 12))
    dates, values, total_12w = forecast_model.get_what_if(growth, weeks)
    return jsonify({'dates': dates, 'values': values, 'total_12w': total_12w})


@dashboard_bp.route('/api/forecast/metrics')
def api_forecast_metrics():
    return jsonify(forecast_model.get_model_metrics())


# ── Segmentation API ──

@dashboard_bp.route('/api/segments/distribution')
def api_segments_distribution():
    return jsonify(rfm_model.get_segment_distribution())


@dashboard_bp.route('/api/segments/summary')
def api_segments_summary():
    df = rfm_model.get_segment_summary()
    return jsonify(df.reset_index().to_dict('records'))


@dashboard_bp.route('/api/segments/profiles')
def api_segments_profiles():
    return jsonify(rfm_model.get_segment_profiles())


# ── Churn API ──

@dashboard_bp.route('/api/churn/summary')
def api_churn_summary():
    return jsonify(churn_model.get_summary())


@dashboard_bp.route('/api/churn/feature-importance')
def api_churn_feature_importance():
    return jsonify(churn_model.get_feature_importance())


@dashboard_bp.route('/api/churn/risk-distribution')
def api_churn_risk_distribution():
    return jsonify(churn_model.get_risk_distribution())


@dashboard_bp.route('/api/churn/retention-playbook')
def api_churn_retention_playbook():
    return jsonify(churn_model.get_retention_playbook())


# ── Inventory API ──

@dashboard_bp.route('/api/inventory/calculate')
def api_inventory_calculate():
    lead_time = int(request.args.get('lead_time', 2))
    service_level = float(request.args.get('service_level', 0.95))
    ordering_cost = float(request.args.get('ordering_cost', 500))
    holding_cost = float(request.args.get('holding_cost', 0.5))
    return jsonify(inventory_model.calculate(lead_time, service_level, ordering_cost, holding_cost))


@dashboard_bp.route('/api/inventory/simulate')
def api_inventory_simulate():
    params = {
        'lead_time': int(request.args.get('lead_time', 2)),
        'reorder_point': float(request.args.get('reorder_point', 30000)),
        'safety_stock': float(request.args.get('safety_stock', 15000)),
        'eoq': float(request.args.get('eoq', 15000)),
    }
    return jsonify(inventory_model.simulate(**params))


@dashboard_bp.route('/api/reports/summary')
def api_reports_summary():
    return jsonify({
        'stats': forecast_model.get_stats(),
        'segments': sum(rfm_model.get_segment_distribution().get('values', [])),
        'churn': churn_model.get_summary()
    })
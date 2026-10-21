from flask import Blueprint, jsonify
from app.services.analytics_service import RiskAnalyticsService
from app.tasks.risk_tasks import run_risk_analysis_task
from app import db

api_bp = Blueprint('api', __name__)

@api_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "RiskLens API",
        "message": "System is operational"
    }), 200

@api_bp.route('/analyze', methods=['POST'])
def trigger_analysis():
    """Triggers the risk analytics job asynchronously via Celery & RabbitMQ."""
    try:

        task = run_risk_analysis_task.delay()
        
        return jsonify({
            "status": "accepted",
            "message": "Risk analysis job queued successfully",
            "task_id": task.id
        }), 202
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@api_bp.route('/reports', methods=['GET'])
def get_reports():
    """Fetches stored analysis reports from MongoDB (PyMongo)."""
    try:
        if db is None:
            return jsonify({"error": "Database not connected"}), 500
            
        reports = list(db.analysis_reports.find({}, {'_id': False}))
        return jsonify({
            "status": "success",
            "count": len(reports),
            "reports": reports
        }), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
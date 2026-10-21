from app.tasks.celery_app import celery_app
from app.services.analytics_service import RiskAnalyticsService
from pymongo import MongoClient
import os
import datetime

@celery_app.task(bind=True)
def run_risk_analysis_task(self):
    """Celery background task to process risk data and save metrics to MongoDB."""
    try:
        service = RiskAnalyticsService()
        metrics = service.load_and_process_data()
        
        mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/risk_lens_db")
        client = MongoClient(mongo_uri)
        db = client.get_database()
        
        task_record = {
            "task_id": self.request.id,
            "status": "COMPLETED",
            "timestamp": datetime.datetime.utcnow(),
            "analytics": metrics
        }
        db.analysis_reports.insert_one(task_record)
        
        return {"status": "success", "task_id": self.request.id}
    except Exception as e:
        return {"status": "error", "message": str(e)}
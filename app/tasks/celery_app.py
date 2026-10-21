from celery import Celery
import os

def make_celery(app_name=__name__):
    broker_url = os.getenv("CELERY_BROKER_URL", "amqp://guest:guest@localhost:5672//")
    result_backend = os.getenv("CELERY_RESULT_BACKEND", "rpc://")
    
    celery = Celery(
        app_name,
        broker=broker_url,
        backend=result_backend,
        include=['app.tasks.risk_tasks']
    )
    return celery

celery_app = make_celery()
from celery import Celery
from datetime import datetime, timedelta
from app.services.aws_cost_explorer import fetch_aws_cost_and_usage
from app.services.anomaly_detection import detect_anomalies
import os

celery_app = Celery(
    'tasks',
    broker=os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0'),
    backend=os.getenv('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')
)

@celery_app.task
def fetch_and_store_aws_costs():
    today = datetime.utcnow().date()
    start_date = (today - timedelta(days=7)).strftime('%Y-%m-%d')
    end_date = today.strftime('%Y-%m-%d')
    fetch_aws_cost_and_usage(start_date, end_date)

@celery_app.task
def run_anomaly_detection():
    detect_anomalies()

# Example: Schedule periodic tasks in Celery Beat (add to celery config)
# celery -A app.tasks.scheduled.celery_app beat --loglevel=info
# (Configure periodic tasks in celeryconfig.py or via the Django/Flask admin)

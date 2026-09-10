# Cloud Cost Optimization Platform (AWS)

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![FastAPI](https://img.shields.io/badge/fastapi-0.100%2B-green)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
 
## Description
A real-time, advanced platform for monitoring, analyzing, and optimizing AWS cloud costs. Features include cost anomaly detection using ML, resource optimization recommendations, budget tracking, and automated cost reporting. Built with FastAPI, Celery, SQLAlchemy, and AWS Cost Explorer API.

## Features
- Real-time AWS cost ingestion and dashboard API
- ML-based cost anomaly detection (Isolation Forest)
- Resource optimization recommendations (EC2, RDS, S3, etc.)
- User-defined budget tracking and alerts
- Automated PDF/CSV cost reporting and email delivery
- Scheduled jobs with Celery
- Modular, extensible backend (ready for Azure/GCP)

## Tech Stack
- Python, FastAPI, SQLAlchemy, Celery, PostgreSQL/SQLite, boto3, scikit-learn, pandas

## Setup & Usage
1. **Clone the repo**
   ```sh
   git clone <repo-url>
   cd Cloud Cost Optimization Platform
   ```
2. **Install dependencies**
   ```sh
   cd backend
   pip install -r requirements.txt
   ```
3. **Set environment variables** (`.env` file or export):
   - `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`
   - `DATABASE_URL` (optional, defaults to SQLite)
   - `CELERY_BROKER_URL` and `CELERY_RESULT_BACKEND` (for Celery)
4. **Initialize the database**
   ```sh
   python -c "from app.database import Base, engine; Base.metadata.create_all(bind=engine)"
   ```
5. **Run the FastAPI server**
   ```sh
   uvicorn app.main:app --reload
   ```
6. **Run Celery worker (for scheduled jobs)**
   ```sh
   celery -A celery_worker.celery_app worker --loglevel=info
   ```

## License
MIT

## Topics
cloud-cost aws cost-optimization fastapi celery anomaly-detection boto3 sqlachemy python cloud-monitoring cloud-billing cost-explorer-api cost-reporting cloud-resource-optimization

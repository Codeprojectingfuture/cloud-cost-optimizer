import pandas as pd
from sklearn.ensemble import IsolationForest
from app.models import CostRecord, Anomaly
from app.database import SessionLocal
from datetime import datetime

def detect_anomalies():
    db = SessionLocal()
    records = db.query(CostRecord).all()
    if not records:
        db.close()
        return
    # Prepare data
    df = pd.DataFrame([
        {"id": r.id, "amount": r.amount, "date": r.date, "service": r.service} for r in records
    ])
    # For each service, detect anomalies
    for service in df['service'].unique():
        sdf = df[df['service'] == service]
        if len(sdf) < 10:
            continue
        model = IsolationForest(contamination=0.1, random_state=42)
        sdf['anomaly'] = model.fit_predict(sdf[['amount']])
        anomalies = sdf[sdf['anomaly'] == -1]
        for _, row in anomalies.iterrows():
            exists = db.query(Anomaly).filter_by(cost_record_id=row['id']).first()
            if not exists:
                anomaly = Anomaly(
                    date=row['date'],
                    service=service,
                    detected_on=datetime.utcnow(),
                    details=f"Cost anomaly detected: ${row['amount']}",
                    cost_record_id=row['id']
                )
                db.add(anomaly)
    db.commit()
    db.close()

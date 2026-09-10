import boto3
import os
from datetime import datetime, timedelta
from app.models import CostRecord
from app.database import SessionLocal

def fetch_aws_cost_and_usage(start_date: str, end_date: str, granularity="DAILY"):
    client = boto3.client(
        "ce",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv("AWS_REGION", "us-east-1")
    )
    response = client.get_cost_and_usage(
        TimePeriod={"Start": start_date, "End": end_date},
        Granularity=granularity,
        Metrics=["UnblendedCost", "UsageQuantity"],
        GroupBy=[{"Type": "DIMENSION", "Key": "SERVICE"}]
    )
    db = SessionLocal()
    for result in response["ResultsByTime"]:
        for group in result["Groups"]:
            service = group["Keys"][0]
            amount = float(group["Metrics"]["UnblendedCost"]["Amount"])
            usage = float(group["Metrics"]["UsageQuantity"]["Amount"])
            cost_record = CostRecord(
                date=datetime.strptime(result["TimePeriod"]["Start"], "%Y-%m-%d").date(),
                service=service,
                amount=amount,
                usage=usage,
                user_id=1  # For demo, assign to user 1
            )
            db.add(cost_record)
    db.commit()
    db.close()

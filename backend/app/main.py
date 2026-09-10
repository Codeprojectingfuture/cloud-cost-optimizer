from fastapi import FastAPI
from app.api import cost, budget, anomaly, optimize

app = FastAPI(title="AWS Cost Optimization Platform")

# Include routers for modular APIs
app.include_router(cost.router, prefix="/cost", tags=["Cost"])
app.include_router(budget.router, prefix="/budget", tags=["Budget"])
app.include_router(anomaly.router, prefix="/anomaly", tags=["Anomaly"])
app.include_router(optimize.router, prefix="/optimize", tags=["Optimization"])

@app.get("/")
def root():
    return {"message": "AWS Cost Optimization Platform is running."}

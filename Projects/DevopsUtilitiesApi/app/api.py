from fastapi import FastAPI
from routers import metrics
from routers import aws

app = FastAPI(
    title="Internal DevOps Utilities API",
    description="API for various DevOps utilities",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

@app.get("/")
def hello():
    """
    This is hello api, just for testing
    """
    return {"message": "Hello, Dosto, This is devops utilities API!"}

app.include_router(metrics.router)
app.include_router(aws.router,prefix="/aws")




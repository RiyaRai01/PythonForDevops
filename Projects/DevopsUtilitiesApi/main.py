from app.api import app
import uvicorn

#Entry point of the application
if __name__ == "__main__":
    ##ASGI
    uvicorn.run(
        "app.api:app",
        host="0.0.0.0", 
        port=8269,
        reload=True
    )
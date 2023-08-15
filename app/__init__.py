from fastapi import FastAPI

from app.api.routes.test_router import router as test_router

# Initiate FastAPI app
app = FastAPI(title="Your API", version="0.1")

# Integrate all router you have
app.include_router(test_router)

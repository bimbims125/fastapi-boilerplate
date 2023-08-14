from fastapi import FastAPI

from app.api.routes.test_router import router as test_router
app = FastAPI()

app.include_router(test_router)

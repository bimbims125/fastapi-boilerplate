from fastapi import APIRouter
from app.api.crud.test_crud import test, test_2

router = APIRouter(prefix="/api/v1")

router.add_api_route(
  "/test",
  test,
  methods=["GET"]
)

router.add_api_route(
  "/test/{id}",
  test_2,
  methods=["GET"]
)

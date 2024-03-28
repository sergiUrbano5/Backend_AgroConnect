from app.backend.database import SessionLocal
from app.schemas.user import UserCreate
from app.services.crud_user import create_user
import pytest

db = SessionLocal()


def test_insert_user():
    test_user = UserCreate(email="example@gmail.com", password="12345678", full_name="test", company_id=1)
    print(test_user)
    app_user = create_user(db, test_user)
    db.close()
    return app_user


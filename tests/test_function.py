from backend.crud import get_products
from sqlalchemy.orm import Session

def test_get_products_empty_db(test_db: Session):
    products = get_products(db=test_db)
    assert products == []
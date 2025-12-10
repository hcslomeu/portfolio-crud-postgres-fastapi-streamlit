from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schemas import ProductResponse, ProductUpdate, ProductCreate
from typing import List
from crud import (
    create_product,
    get_products,
    get_product,
    delete_product,
    update_product,
)

router = APIRouter()

# create route to fetch all items
# required attributes: PATH and RESPONSE
@router.get(path="/products/", response_model=List[ProductResponse])
def read_all_products_route(db: Session = Depends(get_db)):
    """"
    this function will read all the products in the database
    """
    products = get_products(db)
    return products

# create route to fetch 1 item
@router.get(path="/products/", response_model=ProductResponse)
def read_single_product_route(product_id: int, db: Session = Depends(get_db)):
    db_product = get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="the items does not exist")
    return db_product

# create route to add 1 item
@router.post(path="/products/", response_model=ProductResponse)
def create_product_route(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(product=product, db=db)

# create route to delete 1 item
@router.delete(path="/products/{product_id}", response_model=ProductResponse)
def delete_product_route(product_id: int, db: Session = Depends(get_db)):
    product_db = delete_product(product_id=product_id, db=db)
    if product_db is None:
        raise HTTPException(status_code=404, detail="the item you want to delete does not exist")
    
    return product_db

# create route to update items
@router.put(path="/products/{product_id}", response_model=ProductResponse)
def update_product_route(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    product_db = update_product(db=db, product_id=product_id, product=product)
    if product_db is None:
        raise HTTPException(status_code=404, detail="the item you want to update does not exist")
    
    return product_db
from .models import ProductModel
from .schemas import ProductCreate, ProductUpdate
from sqlalchemy.orm import Session


# get all (select * from)
def get_products(db: Session):
    """
    This function returns all the products in the table Product

    """
    return db.query(ProductModel).all()


# get where id=1
def get_product(db: Session, product_id: int):
    """
    This function returns a single product in the table Product

    """
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()


# insert into (create)
def create_product(db: Session, product: ProductCreate):
    # transform view into ORM
    db_product = ProductModel(**product.model_dump())
    # add to table
    db.add(db_product)
    # commit changes on table
    db.commit()
    # refresh the db
    db.refresh(db_product)
    # return created item to user
    return db_product


# delete where id = 1
def delete_product(db: Session, product_id: int):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    db.delete(db_product)
    db.commit()
    return db_product


def update_product(db: Session, product_id: int, product: ProductUpdate):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    if db_product is None:
        return None

    if product.name is not None:
        db_product.name = product.name

    if product.description is not None:
        db_product.description = product.description

    if product.price is not None:
        db_product.price = product.price

    if product.category is not None:
        db_product.category = product.category

    if product.email_supplier is not None:
        db_product.email_supplier = product.email_supplier

    db.commit()
    db.refresh(db_product)
    return db_product

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, PositiveFloat


class ProductBase(BaseModel):

    name: str
    description: str
    price: PositiveFloat
    category: str
    email_supplier: EmailStr


class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ProductUpdate(ProductBase):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[PositiveFloat] = None
    category: Optional[str] = None
    email_supplier: Optional[EmailStr] = None

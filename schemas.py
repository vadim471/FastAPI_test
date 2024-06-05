from pydantic import BaseModel

class Color(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    nm_id: int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    name: str
    brand: str
    brand_id: int
    site_brand_id: int
    supplier_id: int
    sale: float | None = None
    price: int | None = None
    sale_price: int | None = None
    rating: float
    feedbacks: int
    colors: list[Color] = []

    class Config:
        orm_mode = True

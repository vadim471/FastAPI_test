from typing import List
from .database import Base
from sqlalchemy import ForeignKey, Integer, String, Float, Column, Table
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy import orm

products_colors = Table(
    "products_colors",
    Base.metadata,
    Column("product_id", ForeignKey("products.nm_id")),
    Column("color_id", ForeignKey("colors.id")),
)

class Color(Base):
    __tablename__ = 'colors'
    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String)

    products: Mapped[List["Product"]] = relationship(secondary=products_colors, back_populates='colors')
    
class Product(Base):
    __tablename__ = 'products'
    nm_id = Column(Integer, primary_key=True)
    name = Column(String)
    brand = Column(String)
    brand_id = Column(Integer)
    site_brand_id = Column(Integer)
    supplier_id = Column(Integer)
    price = Column(Integer)
    sale_price = Column(Integer)
    rating = Column(Float)
    feedbacks = Column(Integer)
    
    colors: Mapped[List["Color"]] = relationship(secondary=products_colors, back_populates='products', uselist=True)
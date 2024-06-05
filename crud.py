from sqlalchemy.orm import Session
from . import models, schemas
from .services import get_product_from_wb, parse_product

def add_product(session:Session, id:int):
    product_json = get_product_from_wb(id)
    product = parse_product(product_json)
    db_product = models.Product(nm_id=product.nm_id, 
                                name=product.name,
                                brand=product.brand,
                                brand_id=product.brand_id,
                                site_brand_id=product.site_brand_id,
                                supplier_id=product.supplier_id,
                                price=product.price,
                                sale_price=product.sale_price,
                                rating=product.rating,
                                feedbacks=product.feedbacks,
                                )
   
    for color in product.colors:
        db_color = models.Color(id=color.id, name=color.name)
        db_product.colors.append(db_color)
    

    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product

def get_product(session:Session, id:int) -> models.Product:
    return session.query(models.Product).filter(models.Product.nm_id == id).first()


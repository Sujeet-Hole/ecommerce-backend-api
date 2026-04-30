from sqlalchemy import Column, Integer, String, Text, Numeric, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False, index=True)
    slug = Column(String(180), unique=True, nullable=False, index=True)
    description = Column(Text)

    price = Column(Numeric(10, 2), nullable=False)
    stock = Column(Integer, default=0)

    sku = Column(String(100), unique=True, nullable=False)

    is_active = Column(Boolean, default=True)

    category_id = Column(Integer, ForeignKey("categories.id", ondelete="SET NULL"))

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    category = relationship("Category", back_populates="products")
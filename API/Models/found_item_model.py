from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, Date
from sqlalchemy.orm import relationship


from pydantic import BaseModel

from ..database import Base


class Found_Item(Base):
    __tablename__ = "found_items"

    found_items_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=20))
    found_lattitude = Column(Float)
    found_longitudee = Column(Float)
    found_date = Column(Date)
    user_id = Column(Integer, ForeignKey("users.user_id"))

    # users = relationship("User", back_populates="found_items")
    # lost_items = relationship("Lost_Item", back_populates="found_items")
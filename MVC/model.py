from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, validates
import re


Base = declarative_base()


class EmailAddress(Base):
    pass
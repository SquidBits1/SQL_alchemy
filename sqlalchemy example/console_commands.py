from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model import Person, Activity

engine = create_engine('sqlite:///activities.sqlite', echo=True)
sess = Session(engine)
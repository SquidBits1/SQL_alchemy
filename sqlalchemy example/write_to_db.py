from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model import Person, Activity


people = [Person(first_name="Daryl", last_name="Noyce"),
          Person(first_name="Gilad", last_name="Smith"),
          Person(first_name='Katya', last_name="Warner")]

chess = Activity(name='Chess')
fives = Activity(name='Fives')
outdoor_ed = Activity(name='Outdoor Ed')

people[0].activities.append(chess)
people[0].activities.append(fives)
people[1].activities.append(outdoor_ed)
people[1].activities.append(fives)

engine = create_engine('sqlite:///activities.sqlite', echo=True)

with Session(engine) as sess:
    sess.add_all(people)
    sess.commit()
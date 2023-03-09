from sqlalchemy import Column, Integer, String, Table, UniqueConstraint, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

person_activity = Table('person_activity',
                        Base.metadata,
                        Column('id', Integer, primary_key=True),
                        Column('activity_id', ForeignKey('activity.id')),
                        Column('person_id', ForeignKey('person.id')),
                        UniqueConstraint('activity_id', 'person_id'))


class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True, autoincrement=True)
    room = Column(String, unique=True, nullable=False)
    activities = relationship("Activity", backref="location")


class Activity(Base):
    __tablename__ = 'activity'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    location_id = Column(Integer, ForeignKey("location.id"), default=None)
    attendees = relationship("Person",
                             secondary=person_activity,
                             order_by='(Person.last_name, Person.first_name)',
                             back_populates='activities')

    def __repr__(self):
        return f'<Activity({self.name})>'


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    activities = relationship("Activity",
                              secondary=person_activity,
                              order_by='Activity.name',
                              back_populates='attendees'
                              )

    def __repr__(self):
        return f'Person({self.first_name} {self.last_name})'

    def greeting(self):
        print(f'{self.first_name} says "hello"!')

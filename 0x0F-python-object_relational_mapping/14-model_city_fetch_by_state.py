#!/usr/bin/python3
"""
class definition of a State and an instance Base = declarative_base():
"""
from sys import argv
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in (session.query(State.name, City.id, City.name)
                     .filter(State.id == City.state_id)):
        print('{}: ({}) {}'.format(instance[0], instance[1], instance[2]))
    session.commit()
    session.close()

#!/usr/bin/python3
"""
This script prints the state and  its
corresponding city data from the database
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for st in session.query(State).order_by(State.id):
        print("{}: {}".format(st.id, st.name))
        for c in st.cities:
            print("    {}: {}".format(c.id, c.name))

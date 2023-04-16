#!/usr/bin/python3
"""
A script that  prints all City objects from
the database hbtn_0e_14_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import Base, City
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    x = session.query(City, State).filter(City.state_id == State.id)\
        .order_by(City.id).all()
    for city, state in x:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

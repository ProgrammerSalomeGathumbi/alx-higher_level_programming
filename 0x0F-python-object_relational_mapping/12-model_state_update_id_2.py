#!/usr/bin/python3
"""
A script that changes the name of a
State object from the database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    change_state = session.query(State).filter_by(id=2).first()
    change_state.name = "New Mexico"
    change_state.id = 2
    session.commit()

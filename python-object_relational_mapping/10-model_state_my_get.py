#!/usr/bin/python3
"""
Prints the State object with the name passed as an argument
from the database hbtn_0e_6_usa.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    # Create an engine that connects to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create a session and query the State object by name
    session = Session(engine)
    state = session.query(State).filter_by(name=argv[4]).first()

    # Print the result or 'Not found' if no such state exists
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()


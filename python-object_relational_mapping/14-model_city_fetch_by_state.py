#!/usr/bin/python3 

#!/usr/bin/python3

"""
Lists all City objects from the database hbtn_0e_14_usa along with
their associated State.

Usage: ./14-model_city_fetch_by_state.py <mysql username> <mysql
password> <database name>

This script connects to a MySQL database and fetches all City objects
along with their associated State objects. It prints the output in
the format: <state name>: (<city id>) <city name>.

Imports:
    - sys: Provides access to command-line arguments.
    - create_engine: Creates a new SQLAlchemy engine for connecting to
      the database.
    - sessionmaker: Creates a new SQLAlchemy session.
    - State: SQLAlchemy model for the states table.
    - City: SQLAlchemy model for the cities table.

Script Workflow:
1. Create an SQLAlchemy engine to connect to the MySQL database using
   provided credentials.
2. Create a session to interact with the database.
3. Query all City and State objects, joining them on the state_id.
4. Print each city's id and name, along with the name of its state.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

if __name__ == "__main__":
    # Create an SQLAlchemy engine to connect to the MySQL database
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query City and State objects, joining them on state_id
    for city, state in session.query(City, State) \
                              .filter(City.state_id == State.id) \
                              .order_by(City.id):
        # Print city and state information
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close the session
    session.close()

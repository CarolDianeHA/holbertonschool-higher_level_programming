#!/usr/bin/python3

"""Lists all State objects from the database hbtn_0e_6_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """Gather user input for MySQL credentials."""
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    # state = sys.argv[4]
    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    url = url.format(user, password, db_name)

    """Create the engine and session."""
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).order_by(State.id)
    states = query.all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

#!/usr/bin/python3

"""Changes the name of a State object in the database."""

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

    state = session.query(State).filter(State.id == 2).first()
    if state:
        state.name = "New Mexico"
        session.commit()
    else:
        print("Not found")

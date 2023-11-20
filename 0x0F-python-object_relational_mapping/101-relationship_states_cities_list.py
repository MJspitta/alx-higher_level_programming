#!/usr/bin/python3
"""script that lists all State objects, and
corresponding City objects, contained in the database
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    row = session.query(State).order_by(State.id).all()
    for s in row:
        print("{}: {}".format(s.id, s.name))
        for c in s.cities:
            print("    {}: {}".format(c.id, c.name))
    session.close()

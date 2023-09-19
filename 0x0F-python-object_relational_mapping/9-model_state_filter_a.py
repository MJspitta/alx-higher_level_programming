#!/usr/bin/python3
"""lists all State objects that contain the letter a from database
"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(user, passwd, db), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states_a = session.query(State).filter(
            State.name.like("%a%")).order_by(State.id)
    for s in states_a:
        print("{:d}: {:s}".format(s.id, s.name))

    session.close()

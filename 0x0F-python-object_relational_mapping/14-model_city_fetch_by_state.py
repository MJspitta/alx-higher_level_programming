#!/usr/bin/python3
"""prints all City objects from the database"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(user, passwd, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(State.name, City.id, City.name).filter(
            State.id == City.state_id).order_by(City.id)
    for c in cities:
        print("{:s}: ({:d}) {:s}".format(c[0], c[1], c[2]))
    session.close()

#!/usr/bin/python3

"""Doc"""

from model_state import State, Base
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3], pool_pre_ping=True))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    firstState = session.query(State).first()
    if firstState is None:
        print("Nothing")
    else:
        print(f'{firstState.id}: {firstState.name}')

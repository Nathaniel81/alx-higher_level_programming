#!/usr/bin/python3

"""Doc"""

from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    argState = session.query(State).filter(State.name == argv[4])
    print(argState.id) if (argState) else print("Not found")

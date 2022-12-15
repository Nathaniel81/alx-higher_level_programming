#!/usr/bin/python3

"""Doc"""

from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(City).order_by(City.id)
    for city in result:
        print(f'{city.id}: {city.name} -> {city.state.name}')

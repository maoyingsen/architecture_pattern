import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers

from orm import metadata, start_mappers

"""
@pytest.fixture
def in_memory_db():
    engine = create_engine('sqlite:///:memory:')
    metadata.create_all(engine)
    return engine


@pytest.fixture
def session(in_memory_db):
    start_mappers()
    yield sessionmaker(bind=in_memory_db)()
    clear_mappers()

"""
@pytest.fixture
def session_in_memory_db():
    engine = create_engine('sqlite:///:memory:')
    metadata.create_all(engine)
    start_mappers()
    return sessionmaker(bind=engine)()

@pytest.fixture
def session_db():
    engine = create_engine('sqlite:///D:\\tutorial\\Architecture_Patterns_with_Python\\coding\\cha4\\db_test.db')
    metadata.create_all(engine)
    start_mappers()
    return sessionmaker(bind=engine)()
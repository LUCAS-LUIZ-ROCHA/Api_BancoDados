import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from bd_crud.app import app
from bd_crud.models import Base


@pytest.fixture
def client():
    return TestClient(app)


"""Aqui estou criando uma fixture para deixar o código mais limpo e não
 ficar repetindo client = TestClient(app) no teste, assim evitando 
 o DRY 'Não se repetir' """


@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    yield Session()
    Base.metadata.drop_all(engine)

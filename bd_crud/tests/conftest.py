import pytest
from fastapi.testclient import TestClient

from bd_crud.app import app


@pytest.fixture
def client():
    return TestClient(app)


"""Aqui estou criando uma fixture para deixar o código mais limpo e não
 ficar repetindo client = TestClient(app) no teste, assim evitando 
 o DRY 'Não se repetir' """

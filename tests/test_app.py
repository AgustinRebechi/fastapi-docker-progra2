from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_debe_devolver_ok_y_hola_mundo():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Hola Mundo!'} # Assert

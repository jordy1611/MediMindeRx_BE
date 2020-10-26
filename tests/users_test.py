import pytest
import json

from run import create_app


@pytest.fixture
def app():
    


@pytest.fixture
def client(app):
    return app.test_client()


def test_user_index(app, client):
    res = client.get('/Hello')
    assert res.status_code == 200
    expected = {"message": "Hello, World!"}
    assert expected == json.loads(res.get_data(as_text=True))

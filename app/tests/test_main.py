import pytest
from starlette.testclient import TestClient

from app import main

client = TestClient(main.app)

# tests prediction route with sample url param
# @pytest.fixture(scope="module")
def test_predict_iris(test_app):
    response = client.get("/predict?s_length=5.7&s_width=5.6&p_length=4.3&p_width=5.0")
    assert response.status_code == 200


# test with a string as url param, not a valid float, should fail
def test_predict_iris_str_error(test_app):
    response = client.get(
        "http://127.0.0.1:8000/predict?s_length=5.7&s_width=5.6&p_length=4.3&p_width=foo"
    )
    assert response.status_code == 422
    assert response.json()["detail"] == [
        {
            "loc": ["query", "p_width"],
            "msg": "value is not a valid float",
            "type": "type_error.float",
        }
    ]

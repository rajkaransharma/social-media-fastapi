import pytest
from jose import jwt
from app import schemas
from app.config import settings


# def test_root(client):
#     res = client.get("/")
#     print(res.json().get('message'))
#     assert res.json().get('message') == 'Please check /docs for more details.'
#     assert res.status_code == 200

def test_create_user(client):
    res = client.post("/users/", json={"email": "raj@dev.in", "password": "password"})
    
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "raj@dev.in"
    assert res.status_code == 201

def test_login_user(client, test_user):
    res = client.post("/login", data={"username": test_user['email'], "password": test_user['password']})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get('user_id')
    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200

def test_incorrect_login(client):
    res = client.post("/login", data={"username": "raj@dev.in", "password": "IncorrectPassword"})
    assert res.status_code == 403
    # assert res.json().get('detail') == 'Invalid Credentials'



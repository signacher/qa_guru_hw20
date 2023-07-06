from jsonschema.validators import validate
from helper import load_json_schema, reqres_session


def test_create_user_post_validation():
    name = "Ivan"
    job = "quality assurance"
    schema = load_json_schema("post_create_user.json")

    response = reqres_session.post("/api/users", json={"name": name, "job": job})

    validate(instance=response.json(), schema=schema)


def test_update_user_put_validation():
    name = "Ivan"
    job = "automation quality assurance"
    schema = load_json_schema("put_update_user_schema.json")

    response = reqres_session.put("/api/users/490", json={"name": name, "job": job})

    validate(instance=response.json(), schema=schema)


def test_update_user_patch_validation():
    responce = reqres_session.patch('/api/users/2', json={
        "name": "morpheus",
        "job": "zion resident"
    })
    schema = load_json_schema('patch_update_user_validation.json')
    validate(instance=responce.json(), schema=schema)


def test_user_register_successful_validation():
    data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    schema = load_json_schema('post_user_register_successful.json')
    response = reqres_session.post(url=f'/api/register', data=data)

    validate(instance=response.json(), schema=schema)


def test_post_user_register_unsuccessful_validation():
    email = "sydney@fife"
    schema = load_json_schema("post_user_register_unsuccessful.json")

    response = reqres_session.post("/api/register", json={"email": email})

    validate(instance=response.json(), schema=schema)


def test_get_single_resource_validation():
    id_resource = 2
    response = reqres_session.get(f"/api/unknown/{id_resource}")
    schema = load_json_schema("get_single_resource.json")

    validate(instance=response.json(), schema=schema)


def test_get_list_resources_validation():
    response = reqres_session.get("/api/unknown")
    schema = load_json_schema("get_list_resource.json")
    validate(instance=response.json(), schema=schema)


def test_user_not_found_validation():
    schema = load_json_schema('get_user_not_found.json')
    responce = reqres_session.get('/api/users/23')

    validate(instance=responce.json(), schema=schema)


def test_login_success_validation():
    data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = reqres_session.post(url='/api/login', data=data)
    schema = load_json_schema('post_login_success.json')
    validate(instance=response.json(), schema=schema)


def test_login_unsuccess_validation():
    data = {
        "email": "sydney@fifen",
    }
    response = reqres_session.post(url='/api/register', data=data)
    schema = load_json_schema('post_login_unsuccess.json')
    validate(instance=response.json(), schema=schema )
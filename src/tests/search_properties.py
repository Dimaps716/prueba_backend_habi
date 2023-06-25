from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_search_properties_no_filters():
    response = client.get("/property")
    assert response.status_code == 200


def test_search_properties_with_city_filter():
    response = client.get("/property?city=bogota")
    assert response.status_code == 200
    assert len(response.json()) > 1


def test_search_properties_with_address_filter():
    response = client.get("/property?address=carrera 100 #15-90")
    assert response.status_code == 200
    assert len(response.json()) > 1


def test_search_properties_with_year_filter():
    response = client.get("/property?year=2020")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_search_properties_with_multiple_filters():
    response = client.get("/property?city=bogota&year=2011")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_search_properties_with_multiple_values_in_filters():
    response = client.get("/property?city=medellin&city=bogota&address=calle%2023%20%2345-67r&address=calle%2023%20%2345-67q")
    assert response.status_code == 200
    assert len(response.json()) > 0

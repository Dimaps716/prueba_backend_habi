import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from repositories.property import filter_properties

# Crear una conexión a la base de datos de prueba
engine = create_engine("sqlite:///test.db")
Session = sessionmaker(bind=engine)


def setup_function():
    # Configurar la base de datos de prueba con datos iniciales
    with engine.begin() as connection:
        connection.execute(
            "CREATE TABLE property (id INTEGER, city TEXT, year INTEGER, address TEXT, price REAL)"
        )
        connection.execute(
            "INSERT INTO property VALUES (1, 'New York', 2020, '123 Main St', 100000)"
        )
        connection.execute(
            "INSERT INTO property VALUES (2, 'Los Angeles', 2015, '456 Elm St', 200000)"
        )
        connection.execute(
            "INSERT INTO property VALUES (3, 'Miami', 2022, '789 Oak St', 300000)"
        )
        connection.execute(
            "INSERT INTO property VALUES (4, 'New York', 2010, '321 Maple St', 400000)"
        )


def teardown_function():
    # Limpiar la base de datos de prueba
    with engine.begin() as connection:
        connection.execute("DROP TABLE property")


def test_filter_properties_no_filters():
    # Ejecutar la función sin filtros
    results = filter_properties()

    assert len(results) == 4


def test_filter_properties_with_city_filter():
    # Ejecutar la función con filtro de ciudad
    results = filter_properties(city="New York")

    assert len(results) == 2
    assert results[0]["id"] == 1
    assert results[1]["id"] == 4


def test_filter_properties_with_year_filter():
    # Ejecutar la función con filtro de año
    results = filter_properties(year=2020)

    assert len(results) == 1
    assert results[0]["id"] == 1


def test_filter_properties_with_address_filter():
    # Ejecutar la función con filtro de dirección
    results = filter_properties(address="Main St")

    assert len(results) == 1
    assert results[0]["id"] == 1


def test_filter_properties_with_multiple_filters():
    # Ejecutar la función con múltiples filtros
    results = filter_properties(city="New York", year=2010, address="Maple St")

    assert len(results) == 1
    assert results[0]["id"] == 4

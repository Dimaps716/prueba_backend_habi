import logging
from typing import List

from fastapi import HTTPException, status

from repositories.database import create_session


def filter_properties(
    city: str = None, year: int = None, address: str = None
) -> List[dict]:
    """
    Filters available properties based on the specified filters.

    Args:
        city (str, optional): City of the property. (Optional filter)
        construction_year (int, optional): Construction year of the property. (Optional filter)
        address (str, optional): Address of the property. (Optional filter)

    Returns:
        List[dict]: List of filtered properties.

    """
    method = filter_properties.__name__
    db = create_session()
    try:
        query = """
            SELECT p.*, e.name AS status_name
            FROM property AS p
            INNER JOIN status_history AS he ON p.id = he.property_id
            INNER JOIN status AS e ON he.status_id = e.id
            WHERE e.name IN ('pre_venta', 'en_venta', 'vendido')
            AND p.price > 0
        """

        if city:
            query += " AND p.city = '{}'".format(city)

        if year:
            query += " AND p.year = {}".format(year)

        if address:
            cleaned_address = address.replace("'", "''").replace('"', '""')
            query += " AND p.address LIKE '%{}%'".format(cleaned_address)

        # Ejecutar la consulta y obtener los resultados
        results = db.execute(query)

        # Convertir los resultados en una lista de diccionarios
        properties = [dict(row) for row in results]

        return properties

    except Exception as ex:
        logging.error(f"{method}: {ex}")
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"error {method}")

    finally:
        db.close()

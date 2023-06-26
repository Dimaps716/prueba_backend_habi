import logging
from typing import List

from fastapi import HTTPException, status

from repositories.database import create_session


from typing import List

def filter_properties(city: List[str] = None, year: List[int] = None, address: List[str] = None) -> List[dict]:
    """
    Filters available properties based on the specified filters.

    Args:
        city (List[str], optional): Cities of the properties. (Optional filter)
        year (List[int], optional): Construction years of the properties. (Optional filter)
        address (List[str], optional): Addresses of the properties. (Optional filter)

    Returns:
        List[dict]: List of filtered properties.

    """

    method = filter_properties.__name__
    db = create_session()
    try:
        query = """
            SELECT DISTINCT p.id, p.address, p.city, p.price, p.description, p.year, e.name AS status_name
            FROM property AS p
            INNER JOIN (
                SELECT property_id, MAX(update_date) AS max_date
                FROM status_history
                GROUP BY property_id
            ) AS latest ON p.id = latest.property_id
            INNER JOIN status_history AS he ON p.id = he.property_id AND latest.max_date = he.update_date
            INNER JOIN status AS e ON he.status_id = e.id
            WHERE e.name IN ('pre_venta', 'en_venta', 'vendido')
            AND p.price > 0
        """

        if city:
            query += " AND p.city IN :cities"

        if year:
            query += " AND p.year IN :years"

        if address:
            query += " AND ("
            for i, a in enumerate(address):
                if i > 0:
                    query += " OR "
                query += "p.address LIKE :address{}".format(i)
            query += ")"

        params = {
            "cities": city,
            "years": year,
        }

        if address is not None:
            params.update({"address{}".format(i): "%{}%".format(a) for i, a in enumerate(address)})

        # Ejecutar la consulta y obtener los resultados
        results = db.execute(query, params)

        # Convertir los resultados en una lista de diccionarios
        properties = [dict(row) for row in results]

        return properties

    except Exception as ex:
        logging.error(f"{method}: {ex}")
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Error {method}")

    finally:
        db.close()

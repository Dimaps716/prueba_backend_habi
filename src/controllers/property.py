from typing import List

from fastapi import APIRouter, Query, status

from repositories.property import filter_properties

router = APIRouter()


@router.get(
    "/property",
    tags=["property"],
    status_code=status.HTTP_200_OK,
)
def search_properties(
    city: str = Query(None, description="Filter by city of the property"),
    address: str = Query(None, description="Filter by address of the property"),
    year: int = Query(None, description="Filter by construction year of the property"),
):
    """
    Searches for available properties based on the specified filters.

    Args:
        city (str, optional): City of the property. (Optional filter)
        address (str, optional): Address of the property. (Optional filter)
        construction_year (int, optional): Construction year of the property. (Optional filter)

    Returns:
        List[PropertySchema]: List of filtered properties.

    Raises:
        HTTPException: Raised if an error occurs during the query.

    """
    return filter_properties(city=city, address=address, year=year)

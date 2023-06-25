from fastapi import APIRouter, status

router = APIRouter()


@router.get(
	"/property/{property_id}/like",
	tags=["like"],
	status_code=status.HTTP_200_OK,
)
def like_property(property_id: int):
	""""
	Aquí implementa la lógica para registrar el "me gusta" en la base de datos
	Puedes acceder al ID del inmueble a través de la variable property_id
	"""

	return {"message": "Me gusta registrado exitosamente"}

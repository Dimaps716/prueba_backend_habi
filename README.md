# prueba_backend_habi

## Tecnologías utilizadas
- Lenguaje de programación: Python
- Base de datos: MySQL
- Framework web: FASTAPY (utilizado para enrutamiento y manejo de solicitudes HTTP)
- Pruebas unitarias: pytest

## Enfoque para el desarrollo
1. Configuración del entorno:
   - Instalación de Python, MySQL y otras dependencias necesarias.
   - Creación de un entorno virtual para el proyecto.

2. Diseño de la base de datos:
   - Análisis de los requerimientos y creación de un diagrama de Entidad-Relación para el modelo de base de datos.
   - Modificación del modelo actual para soportar la funcionalidad de "Me gusta" y mejorar el rendimiento de las consultas.

3. Implementación del servicio de consulta:
   - Configuración de la conexión a la base de datos.
   - Creación de los endpoints REST para la consulta de inmuebles.
   - Implementación de la lógica de consulta y filtrado de inmuebles.
   - Validación de los datos de entrada y manejo de errores.
   - Pruebas unitarias para verificar el correcto funcionamiento.

4. Implementación del servicio de "Me gusta":
   - Modificación del modelo de base de datos para almacenar los "me gusta" de los usuarios.
   - Creación de los endpoints REST para gestionar los "me gusta".
   - Implementación de la lógica para registrar y consultar los "me gusta" de los usuarios.
   - Validación de los datos de entrada y manejo de errores.
   - Pruebas unitarias para verificar el correcto funcionamiento.

5. Pruebas unitarias adicionales:
   - Creación de pruebas unitarias exhaustivas para todas las funcionalidades implementadas.
   - Verificación de los casos de éxito y los casos de manejo de errores.

6. Documentación:
   - Actualización del archivo README con instrucciones de instalación, configuración y ejecución del proyecto.
   - Inclusión del diagrama de Entidad-Relación y el código SQL para extender el modelo de base de datos.
   - Explicación de las decisiones tomadas durante el desarrollo.

7. Revisión y pulido:
   - Revisión del código para garantizar su calidad, legibilidad y cumplimiento de las guías de estilo.
   - Optimización del rendimiento y manejo de excepciones.
   - Aseguramiento de que todas las funcionalidades se cumplan correctamente.


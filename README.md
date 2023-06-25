# Prueba Backend Habi

## Tecnologías utilizadas
- Lenguaje de programación: Python
- Base de datos: MySQL
- Framework web: FastAPY (utilizado para enrutamiento y manejo de solicitudes HTTP)
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

# Extensión de la base de datos para registrar el histórico de "me gusta"

## Pasos a seguir

1. Crea una nueva tabla llamada "Likes" que almacenará la información de los "me gusta". Esta tabla contendrá los siguientes campos:

   - `id`: Identificador único del "me gusta".
   - `user_id`: ID del usuario que dio el "me gusta".
   - `property_id`: ID del inmueble al que se le dio el "me gusta".
   - `date_liked`: Fecha y hora en la que se dio el "me gusta".

2. Establece las relaciones entre las tablas existentes y la tabla "Likes". Se Puedes elegir una de las siguientes opciones:

   - **Relación uno a muchos entre la tabla "Users" y la tabla "Likes":**
     - Un usuario puede dar varios "me gusta" a diferentes inmuebles.
     - En la tabla "Likes", agrega una clave foránea `user_id` que se relacione con la columna `id` de la tabla "Users".

   - **Relación uno a muchos entre la tabla "Properties" y la tabla "Likes":**
     - Un inmueble puede recibir varios "me gusta" de diferentes usuarios.
     - En la tabla "Likes", agrega una clave foránea `property_id` que se relacione con la columna `id` de la tabla "Properties".
             
     -         +------------------+
               |       Users      |
               +------------------+
               | id (PK)          |
               | name             |
               | email            |
               | ...              |
               +------------------+
                      |
                      |
                      |
               +------------------+
               |     Properties   |
               +------------------+
               | id (PK)          |
               | address          |
               | city             |
               | price            |
               | ...              |
               +------------------+
                      |
                      |
                      |
               +------------------+
               |       Likes      |
               +------------------+
               | id (PK)          |
               | user_id (FK)     |
               | property_id (FK) |
               | date_liked       |
               +------------------+

   - ### Creación de la tabla "Likes"

   ```sql
   CREATE TABLE Likes (
       id INT PRIMARY KEY AUTO_INCREMENT,
       user_id INT,
       property_id INT,
       date_liked DATETIME,
       FOREIGN KEY (user_id) REFERENCES Users(id),
       FOREIGN KEY (property_id) REFERENCES Properties(id)
   );
   ```


# Explicación de la solución

La extensión de la base de datos mediante la creación de una tabla separada llamada "Likes" y estableciendo las relaciones adecuadas ofrece una solución eficiente y escalable para registrar el histórico de "me gusta" de cada usuario y los inmuebles a los que han dado "me gusta". A continuación se presentan las razones por las que considero que esta es la mejor solución:

1. **Normalización de la base de datos**: Al crear una tabla separada para almacenar los "me gusta", seguimos el principio de normalización de la base de datos. Esto nos permite evitar la duplicación de datos y garantizar que cada entidad tenga su propia tabla, lo que facilita la gestión y el mantenimiento de la base de datos.

2. **Relaciones establecidas**: Al establecer las relaciones entre la tabla "Likes" y las tablas existentes de "Users" y "Properties", creamos asociaciones claras y coherentes. Esto nos permite rastrear fácilmente los "me gusta" de un usuario específico y los inmuebles que han recibido "me gusta" de varios usuarios.

3. **Flexibilidad y escalabilidad**: Al separar los "me gusta" en una tabla aparte, podemos realizar consultas y análisis específicos relacionados con esta actividad. Podemos obtener información como el número total de "me gusta" para un inmueble, los inmuebles más populares en función de los "me gusta", o los usuarios que han dado más "me gusta". Esto proporciona flexibilidad para adaptarse a futuras necesidades y permite el crecimiento y escalabilidad del sistema.

4. **Rendimiento optimizado**: Al establecer índices adecuados en las tablas, podemos mejorar el rendimiento de las consultas relacionadas con los "me gusta". Esto garantiza que las consultas sean eficientes y rápidas, incluso cuando haya un gran volumen de datos.

5. **Claridad en el diseño**: Al actualizar el diagrama de Entidad-Relación y documentar claramente los cambios realizados, se proporciona una representación visual y una explicación de la estructura de la base de datos. Esto facilita la comprensión y colaboración entre los miembros del equipo, así como el mantenimiento futuro de la base de datos.

En resumen, la creación de una tabla separada para almacenar los "me gusta" y establecer las relaciones adecuadas ofrece una solución eficiente, escalable y bien estructurada para registrar el histórico de "me gusta" en la base de datos.

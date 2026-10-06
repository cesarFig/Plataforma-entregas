## Reto 1

### Evidencias de César
![Entorno y comandos - César](./imagenesCesar/image-1.png)
![Ejecución de servidor - César](./imagenesCesar/image-2.png)

### Evidencias de Annatar
![Entorno y comandos - Annatar](./imagenesAnnatar/image-1.png)
![Ejecución de servidor - Annatar](./imagenesAnnatar/image-2.png)

### Evidencias de Merali
![Entorno y comandos - Merali](./imagenesMerali/reto1-1.png)
![Ejecución de servidor - Merali](./imagenesMerali/reto1-2.png)

### Evidencias de Daniel
![Entorno y comandos - Daniel](./imagenesDaniel/reto1-1.png)
![Ejecución de servidor - Daniel](./imagenesDaniel/reto1-2.png)

> **Nota del equipo:** Todos los integrantes trabajamos sobre entorno Windows.

---

## Reto 2

### Evidencias de César

#### Código de `reglas.py`
![Código reglas.py - César](./imagenesCesar/image-3.png)

#### Salidas de pruebas
![Salida de prueba 1 - César](./imagenesCesar/image-4.png)
![Salida de prueba 2 - César](./imagenesCesar/image-5.png)
![Salida de prueba 3 - César](./imagenesCesar/image-6.png)

---

### Evidencias de Annatar

#### Código de `reglas.py`
![Código reglas.py - Annatar](./imagenesAnnatar/image-3.png)

#### Salidas de pruebas
![Salida de prueba 1 - Annatar](./imagenesAnnatar/image-4.png)
![Salida de prueba 2 - Annatar](./imagenesAnnatar/image-5.png)
![Salida de prueba 3 - Annatar](./imagenesAnnatar/image-6.png)

---

### Evidencias de Merali

#### Código de `reglas.py`
![Código reglas.py - Merali](./imagenesMerali/reto2-4.png)

#### Salidas de pruebas
![Salida de prueba 1 - Merali](./imagenesMerali/reto2-1.png)
![Salida de prueba 2 - Merali](./imagenesMerali/reto2-2.png)
![Salida de prueba 3 - Merali](./imagenesMerali/reto2-3.png)

---

### Evidencias de Daniel

#### Código de `reglas.py`
![Código reglas.py - Daniel](./imagenesDaniel/reto2-4.png)

#### Salidas de pruebas
![Salida de prueba 1 - Daniel](./imagenesDaniel/reto2-1.png)
![Salida de prueba 2 - Daniel](./imagenesDaniel/reto2-2.png)
![Salida de prueba 3 - Daniel](./imagenesDaniel/reto2-3.png)

---
## Preguntas de Reflexión

### ¿Por qué la validación tiene que estar en el backend, aunque la app móvil ya revise que el campo no esté vacío?
Por **seguridad e integridad de los datos**. Un usuario malintencionado puede saltarse la interfaz móvil y enviar peticiones directamente a la API utilizando herramientas como Postman, cURL o scripts automatizados. Además, al integrar múltiples clientes (web, iOS, Android, etc.), el backend funciona como la única barrera centralizada de defensa, garantizando que no se ingresen datos inválidos o corruptos a la base de datos sin importar la fuente de la petición.

### ¿Qué patrón de los apuntes reemplazaría la cadena de `if` y qué ganarían con eso?
El patrón adecuado para sustituir condicionales de reglas de negocio anidadas es el **Patrón Strategy** o la **Cadena de Responsabilidad (Chain of Responsibility)**.

**Ganancias principales:**
* **Principio de Abierto/Cerrado (Open/Closed Principle):** Permite extender nuevos medios de entrega (como drones o vehículos autónomos) añadiendo nuevas clases o módulos independientes sin modificar el código core existente.
* **Reducción de Complejidad Ciclomática:** Elimina los `if/elif` anidados, facilitando la lectura y mantenimiento del código.
* **Aislamiento y Pruebas Unitarias:** Cada regla de validación se evalúa de forma independiente, lo que simplifica la creación de pruebas unitarias específicas sin riesgo de romper otras reglas.
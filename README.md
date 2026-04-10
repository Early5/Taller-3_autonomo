# Sistema de Gestión de Envíos – Taller Estructuras de Datos

##  Descripción del Taller

Este proyecto resuelve un problema planteado por una empresa de logística que necesita controlar sus envíos en tiempo real. Los problemas planteados son:

- No se puede acceder rápidamente a un envío por su código.
- El orden de los envíos cambia constantemente altas, bajas, reorganizaciones.
- Se requiere recorrer los envíos en ambos sentidos adelante y atrá.
- El sistema actual se vuelve lento cuando crece el volumen de datos.

**Requerimientos técnicos del taller:**
- No usar dict, set, librerías externas ni estructuras avanzadas de Python.
- Implementar manualmente una estructura de datos: lista simplemente enlazada, doblemente enlazada o tabla hash.
- El sistema debe permitir desde consola: agregar, buscar por código, eliminar y mostrar envíos en ambos sentidos.

##  Solución implementada

Se eligió una **lista doblemente enlazada** porque es la única que permite el recorrido bidireccional exigido. La búsqueda es O(n) (lineal), pero para volúmenes moderados de envíos el rendimiento es aceptable y se cumple con todas las restricciones.

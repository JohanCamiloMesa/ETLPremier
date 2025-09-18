# ETLPremier
## Rama Release

### Propósito de la rama
Esta rama contiene la versión estable y lista para producción del proceso ETL para el proyecto Premier. Aquí se consolidan los cambios validados y probados.

### Cambios principales y decisiones técnicas
- Estructuración modular del ETL en carpetas: Extract, Transform, Load y Config.
- Separación de la configuración en `Config/config.py` para facilitar la gestión de parámetros.
- Uso de scripts independientes para cada fase del ETL.
- Integración de archivos fuente en `Extract/Files`.

### Cómo ejecutar el main del ETL
1. Como esta es la estuctura del proyecto, no hay nada que ejecutar, ya que el codigo de desarrollo se vera en la rama de Development
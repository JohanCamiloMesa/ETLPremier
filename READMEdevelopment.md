# ETLPremier

## Desarrollo

### Propósito de la rama
Esta rama está destinada al desarrollo y mejoras en el proceso ETL para la Premier League.

### Cambios principales y decisiones técnicas
- Refactorización de la estructura del proyecto en módulos: Config, Extract, Transform y Load.
- Implementación de clases para la extracción y limpieza de datos.
- Uso de rutas configurables y manejo de archivos CSV.
- Decisiones técnicas orientadas a la modularidad y facilidad de mantenimiento.

### Cómo ejecutar esta parte del ETL
1. Instala las dependencias con `pip install -r requirements.txt`.
2. Ejecuta el archivo principal:
	```powershell
	python main.py
	```
3. El script mostrará el dataset original extraído antes de la limpieza.
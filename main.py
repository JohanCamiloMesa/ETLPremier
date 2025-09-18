from Config.config import Config
from Extract.ETLpremierExtract import ETLpremierExtract                                

# Extracción de datos
extractor = ETLpremierExtract(Config.INPUT_PATH)
extractor.queries()
df = extractor.data


# Mostrar el dataset original completo antes de la limpieza
print("\n--- DATASET ORIGINAL ---\n")
print(df)

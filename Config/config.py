from pathlib import Path

class Config:
    """
    Clase de configuración para rutas y parámetros del ETL.
    """

    BASE_DIR = Path(__file__).parent.parent
    INPUT_PATH = 'D:\\ETLPremier\\Extract\\Files\\England CSV.csv'
    OUTPUT_PATH = 'D:\\ETLPremier\\Extract\\Files\\output_clean.csv'
    SQLITE_DB_PATH = BASE_DIR / 'Extract' / 'Files' / 'ETLpremier.db'
    SQLITE_TABLE = 'ETLpremier_data'
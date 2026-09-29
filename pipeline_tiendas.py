import os
import pandas as pd
from dotenv import load_dotenv
from utils.reglas import limpiar_datos_tienda
from db_utils.load import cargar_dimension_en_db

load_dotenv()

ruta_archivos = os.getenv("RUTA_ARCHIVOS", "csvs")

ruta_archivo_tiendas = os.path.join(ruta_archivos, "tiendas.csv")
datos_brutos_tiendas = pd.read_csv(ruta_archivo_tiendas)

datos_tiendas_limpias = limpiar_datos_tienda(datos_brutos_tiendas)

registros_cargados = cargar_dimension_en_db(datos_tiendas_limpias, tabla="DimTienda")

print(f"¡Proceso exitoso! Se han actualizado {registros_cargados} registros en la dimensión DimTienda.")
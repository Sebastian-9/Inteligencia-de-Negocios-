import os
import pandas as pd
from dotenv import load_dotenv
from utils.reglas import limpiar_datos_producto
from db_utils.load import cargar_dimension_en_db

load_dotenv()

ruta_archivos = os.getenv("RUTA_ARCHIVOS", "csvs")

ruta_archivo_productos = os.path.join(ruta_archivos, "productos.csv")
datos_brutos_productos = pd.read_csv(ruta_archivo_productos)

datos_productos_limpios = limpiar_datos_producto(datos_brutos_productos)

registros_cargados = cargar_dimension_en_db(datos_productos_limpios, tabla="DimProducto")

print(f"¡Proceso exitoso! Se han actualizado {registros_cargados} registros en la dimensión DimProducto.")
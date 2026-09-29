import os
import pandas as pd
from dotenv import load_dotenv
from utils.reglas import limpiar_datos_cliente
from db_utils.load import cargar_dimension_en_db

load_dotenv()

ruta_archivos = os.getenv("RUTA_ARCHIVOS", "csvs")

ruta_archivo_clientes = os.path.join(ruta_archivos, "clientes.csv")
datos_brutos_clientes = pd.read_csv(ruta_archivo_clientes)

datos_clientes_limpios = limpiar_datos_cliente(datos_brutos_clientes)

registros_cargados = cargar_dimension_en_db(datos_clientes_limpios, tabla="DimCliente")

print(f"¡Proceso exitoso! Se han actualizado {registros_cargados} registros en la dimensión DimCliente.")
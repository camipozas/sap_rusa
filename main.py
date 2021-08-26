from selenium_functions import limpiar_output
from params import output_dir
from selenium_functions import descarga
from selenium_functions import consolidar
from sql_server import connection, insert_df

# Credenciales
from params import (
  user_name,
  password,
  driver_path,
  server_sql,
  database,
  user_sql,
  pass_sql
)

# Limpiamos output antes de iniciar
limpiar_output(output_dir)
# Corremos for
sociedades = [2000,2100,2200,3000,3100]

def descargar_recursivo(soc):
  try:
     descarga(soc)
  except:
     descargar_recursivo(soc)

for i in sociedades:
    descargar_recursivo(i)
    print(i)

# Consolidamos en un solo archivo
consolidado = consolidar(output_dir)
consolidado.to_excel('consolidado.xlsx')
print('terminado')

# SQL SERVER
# Cargar funciones SQL
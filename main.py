from selenium_functions import limpiar_output
from params import output_dir
from selenium_functions import descarga
from selenium_functions import consolidar
from sql_server import test
from decorator import log

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
sociedad = [2000,2200,3000,3100]

@log
def descargar_recursivo(sociedad):
  try:
     descarga(sociedad)
  except ValueError("Sin datos en sociedad"):
    raise ValueError("SALTA CUENTA")
  except:
     descargar_recursivo(sociedad)

for i in sociedad:
    try:
      descargar_recursivo(i)
    except:
      print(f"salta sociedad {i}")
      continue
    print(i)

# Consolidamos en un solo archivo
consolidado = consolidar(output_dir)
consolidado.to_excel('consolidado.xlsx')

# SQL SERVER
test(consolidado)    # Guardamos valores en SQL
print('finalizado')
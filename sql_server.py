from sqlalchemy import create_engine
import pandas as pd
from params import server_sql, database, user_sql, pass_sql, mssql_driver
from decorator import log

# Establecemos conexión con SQL Server
@log
def connection():
    engine = create_engine(f'mssql+pyodbc://{user_sql}:{pass_sql}@{server_sql}/{database}?driver={mssql_driver}', 
            fast_executemany = True)
    return engine

# Probamos conexión a SQL Server y la respectiva tabla, si existe reemplazamos los valores.
@log
def test(df):
    engine = connection()
    df.to_sql('sap_rusa', con=engine, if_exists='replace', index=False)
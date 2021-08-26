from sqlalchemy import create_engine
import pandas as pd
from params import server_sql, database, user_sql, pass_sql, mssql_driver

# Establecemos conexión con SQL Server
def connection():
    engine = create_engine(f'mssql+pyodbc://{user_sql}:{pass_sql}@{server_sql}/{database}?driver={mssql_driver}', 
            fast_executemany = True)
    return engine

# Probamos conexión a SQL Server y la respectiva tabla, si existe reemplazamos los valores.
def test(df):
    engine = connection()
    df.to_sql('data_cierre_fbl5n', con=engine, if_exists='replace', index=False)
import psycopg2
from psycopg2 import sql
from constants import DB_CONFIG

def create_db_tables():
    """
    Creates the database tables by executing the SQL script provided in 'create_tables.sql'.
    """
    with open('create_tables.sql', 'r') as f:
        sql_script = f.read()

    try:
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(sql.SQL(sql_script))
                print("The tables are successfully created!")
    except Exception as e:
        print(f"Error during script execution: {e}")
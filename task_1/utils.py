import psycopg2
from psycopg2.extras import RealDictCursor
from tabulate import tabulate
from typing import Any, List
from constants import DB_CONFIG

def execute_query(query, params=None):
    """
    Executes a SQL query against the database.

    Args:
        query (str): The SQL query to execute.
        params (Optional[tuple]): Parameters to bind to the query (default: None).
    """
    try:
        if params is None:
            params = ()

        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(query, params)
                conn.commit()

                if query.strip().lower().startswith("select"):
                    return cur.fetchall()

                return cur.rowcount
    except Exception as e:
        print(f"Error during query execution: {e}")
        return None
    
def display_results(rows: List[Any], title: str = "Results"):
    """
    Displays query results in a tabular format using the tabulate library.

    Args:
        rows (List[Any]): The data rows to display (list of tuples or dictionaries).
        title (str): Title of the results (default: "Results").
    """
    if rows:
        print(f"\n{title}")
        print(tabulate(rows, headers="keys", tablefmt="grid", maxcolwidths=[10, 40, 40]))
    else:
        print(f"No data found for {title}.")
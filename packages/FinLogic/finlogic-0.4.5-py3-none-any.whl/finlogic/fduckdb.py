"""FinLogic Database module."""
from typing import Literal
import duckdb
import pandas as pd
from datetime import datetime
from . import config as cfg

# Start FinLogic Database connection
FINLOGIC_DB_PATH = cfg.DATA_PATH / "finlogic.db"
# Create a new database file and connect to it
con = duckdb.connect(database=f"{FINLOGIC_DB_PATH}")
con.close()


def reset():
    """Delete the database file and create a new one."""
    # Delete database file
    FINLOGIC_DB_PATH.unlink(missing_ok=True)
    # Create a new database file and connect to it
    con = duckdb.connect(database=f"{FINLOGIC_DB_PATH}")
    con.close()


def execute(query: str, convert_to: Literal["df", "fetchall", "fetchone"] = None):
    """Execute a SQL query."""
    results = None
    with duckdb.connect(database=f"{FINLOGIC_DB_PATH}") as con:
        con.execute(query)
        if convert_to == "df":
            results = con.df()
        elif convert_to == "fetchall":
            results = con.fetchall()
        elif convert_to == "fetchone":
            results = con.fetchone()
    return results


def build():
    """Build FinLogic Database from processed CVM files."""
    print("Building FinLogic Database...")
    # Reset database
    reset()
    # Create a table with all processed CVM files
    sql = f"""
        CREATE TABLE reports AS SELECT * FROM '{cfg.CVM_PROCESSED_DIR}/*.parquet'
    """
    execute(sql)


def is_empty() -> bool:
    """Return True if database is considered empty."""
    return FINLOGIC_DB_PATH.stat().st_size / 1024**2 < 10


def get_info() -> dict:
    """Return a dictionary with information about the database."""
    info_dict = {}
    if is_empty():
        return info_dict

    query = """--sql
        SELECT DISTINCT cvm_id, report_type, period_reference
          FROM reports;
    """
    num_of_reports = execute(query, "df").shape[0]
    db_last_modified = datetime.fromtimestamp(FINLOGIC_DB_PATH.stat().st_mtime)
    query = "SELECT COUNT(*) FROM reports"
    number_of_rows = execute(query, "fetchone")[0]
    query = "SELECT MIN(period_end) FROM reports"
    first_statement = execute(query, "fetchone")[0]
    query = "SELECT MAX(period_end) FROM reports"
    last_statement = execute(query, "fetchone")[0]
    query = "SELECT COUNT(DISTINCT cvm_id) FROM reports"
    number_of_companies = execute(query, "fetchone")[0]

    info_dict = {
        "db_path": f"{FINLOGIC_DB_PATH}",
        "db_size": f"{FINLOGIC_DB_PATH.stat().st_size / 1024**2:.2f} MB",
        "db_last_modified": db_last_modified.strftime("%Y-%m-%d %H:%M:%S"),
        "number_of_rows": number_of_rows,
        "number_of_reports": num_of_reports,
        "number_of_companies": number_of_companies,
        "first_report": f"{first_statement}",
        "last_report": f"{last_statement}",
    }

    return info_dict


def get_file_mtimes() -> pd.DataFrame:
    """Return a Pandas DataFrame with unique file_source and file_mtime."""
    if is_empty():
        return pd.DataFrame()

    sql = """
        SELECT DISTINCT file_source, file_mtime
          FROM reports
         ORDER BY file_source
    """
    return execute(sql, "df")

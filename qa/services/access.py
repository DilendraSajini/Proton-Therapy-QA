import pyodbc

def get_connection(db_path:str, password:str):
    return pyodbc.connect(
        rf"DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={db_path};PWD={password};"
    )
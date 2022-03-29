from docarray import DocumentArray
from config import sqlite_filename
import sqlite3


def check_rows_exist(database_name, table_name):
    connection_obj = sqlite3.connect(database_name)
    cursor_obj = connection_obj.cursor()
    cursor_obj.execute(f"SELECT * FROM {table_name}")
    row_count = len(cursor_obj.fetchall())

    if row_count < 1:
        print(f"Table {table_name} is empty")
        return False

    return True


def get_docs(data_source, sqlite_filename=sqlite_filename):
    """
    Pulls DocumentArrays from Jina Cloud so we don't have to compute locally
    """

    table_name = data_source.replace("-", "_")

    sqlite_docs = DocumentArray(
        storage="sqlite",
        config={"connection": sqlite_filename, "table_name": table_name},
    )

    # Only pull data if the database isn't populated
    if not check_rows_exist(sqlite_filename, table_name):  # if table is empty
        da = DocumentArray.pull(data_source, show_progress=True, local_cache=True)
        sqlite_docs.extend(da)

    return sqlite_docs

txt_da = get_docs("ttl-textual")
img_da = get_docs("ttl-embedding")

print(f"ttl-textual: {len(txt_da)} Documents")
print(f"ttl-embeddings: {len(img_da)} Documents")

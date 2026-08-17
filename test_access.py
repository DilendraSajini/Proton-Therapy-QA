from qa.services.access import get_connection
from django.conf import settings

db_path = r"C:\Users\Dwijesin\Desktop\PBT\AssetsDatabase_be.accdb"
password = ""

conn = get_connection(db_path, password)
print("Connected successfully!")
cursor = conn.cursor()
print("\nTables found:\n")
for table in cursor.tables(tableType="TABLE"):
    print(table.table_name)
conn.close()

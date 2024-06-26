import pyodbc

SERVER = 'localhost'
DATABASE = 'icedata'
conn = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes'

conn = pyodbc.connect(conn)
cursor = conn.cursor()


#cursor.close()
#conn.close()

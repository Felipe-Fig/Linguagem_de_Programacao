import seaborn as sns
import sqlite3

cursor = conn.cursor()
cursor.execute(ddl_create)
print(type(cursor))
print("Tabela criada!")
print("Descrição do cursor: ", cursor.description)
print("Linhas afetadas: ", cursor.rowcount)
cursor.close()
conn.close()
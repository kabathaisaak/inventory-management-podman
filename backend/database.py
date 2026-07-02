import psycopg2

connection = psycopg2.connect(
    host="inventory-db",
    database="inventory",
    user="admin",
    password="password",
    port=5432
)

cursor = connection.cursor()
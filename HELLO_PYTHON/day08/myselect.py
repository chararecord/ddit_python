import psycopg2

conn = psycopg2.connect(host="localhost", port="5432", dbname="python", user="postgres", password="python")
cur = conn.cursor()
cur.execute("select col01, col02, col03 from sample;")
rows = cur.fetchall()

print(rows)

cur.close()
conn.close()
import psycopg2

conn = psycopg2.connect(host="localhost", port="5432", dbname="python", user="postgres", password="python")
cur = conn.cursor()

# 멀티라인 허용 """ 멀티 """
sql = """ 
    insert into sample
        (col01, col02, col03)
    values
        ('3','3','3')
"""

cur.execute(sql)
conn.commit()
# rows = cur.fetchall()

# print(rows)

cur.close()
conn.close()
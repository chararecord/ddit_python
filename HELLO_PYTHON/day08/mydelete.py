import psycopg2

col01 = '3'

conn = psycopg2.connect(host="localhost", port="5432", dbname="python", user="postgres", password="python")
cur = conn.cursor()

# 멀티라인 허용 """ 멀티 """
sql = f""" 
    delete from sample
    where
        col01 = '{col01}'
"""

cur.execute(sql)
print("cnt",cur.rowcount)
conn.commit()
# rows = cur.fetchall()

# print(rows)

cur.close()
conn.close()
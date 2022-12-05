import psycopg2

col01 = '4'
col02 = '8'
col03 = '8'

conn = psycopg2.connect(host="localhost", port="5432", dbname="python", user="postgres", password="python")
cur = conn.cursor()

# 멀티라인 허용 """ 멀티 """
sql = f""" 
    update sample
    set
        col02 = '{col02}',
        col03 = '{col03}'
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
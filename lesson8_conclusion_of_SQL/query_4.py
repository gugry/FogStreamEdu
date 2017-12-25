# 4. Получаем список самых активных пользователей, те, у которых больше всего статей.


import psycopg2
from psycopg2 import sql
try:
    conn = psycopg2.connect("dbname='fogstream_rubicon' user='vladislav' host='localhost' password='fog13blik'")
except:
    print ("I am unable to connect to the database")
cur = conn.cursor()
cur.execute("""SELECT COUNT(author.name) as count, author.name from author
INNER JOIN article ON article.author = author.id
GROUP BY author.name
ORDER BY count desc""")

rows = cur.fetchall()
for row in rows:
    if row[0] == rows[0][0]:
        print(row[0], row[1].strip())
conn.commit()

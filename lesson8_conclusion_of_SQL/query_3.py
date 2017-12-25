# 3. Получаем топ 10 популярных хэш-тэгов, т.е. те, у которых больше всего статей/репозиториев;

import psycopg2
from psycopg2 import sql



try:
    conn = psycopg2.connect("dbname='fogstream_rubicon' user='vladislav' host='localhost' password='fog13blik'")
except:
    print ("I am unable to connect to the database")
cur = conn.cursor()
cur.execute("""SELECT COUNT(article_hash.hash) as count, hash.name
FROM article_hash 
INNER JOIN hash ON article_hash.hash = hash.id
GROUP BY article_hash.hash, hash.name
ORDER BY count desc
""")

rows = cur.fetchall()
for row in rows[:10]:
    print(row[0], row[1].strip())
conn.commit()


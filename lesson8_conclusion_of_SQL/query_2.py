#2. Получаем список популярных статей/репозиториев за неделю;

import psycopg2
from psycopg2 import sql
import datetime


date_from = "'" + str(datetime.datetime.today() - datetime.timedelta(days=7)) + "'"
date_to = "'" + str(datetime.datetime.today()) + "'"


try:
    conn = psycopg2.connect("dbname='fogstream_rubicon' user='vladislav' host='localhost' password='fog13blik'")
except:
    print ("I am unable to connect to the database")
cur = conn.cursor()
cur.execute("""SELECT article.id, article.title as hash_name
                   FROM article
                   WHERE article.data > """ + date_from + """ and article.data <""" + date_to)
rows = cur.fetchall()
for row in rows:
    print(row[0], row[1].strip())

conn.commit()

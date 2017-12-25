# 1. Получим список статей/репозиториев по заданному хэш-тэгу в заданный период времени;


import psycopg2
from psycopg2 import sql
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("arg_hash_tag", type=str)
parser.add_argument("arg_date_from", type=str)
parser.add_argument("arg_date_to", type=str)

args = parser.parse_args()
hash_tag = "'" + args.arg_hash_tag + "'"
date_from = "'" + args.arg_date_from + "'"
date_to = "'" + args.arg_date_to + "'"


# hash_tag = "'3d_graphics'"
# date_from = "'2017-12-01'"
# date_to = "'2017-12-05'"


try:
    conn = psycopg2.connect("dbname='fogstream_rubicon' user='vladislav' host='localhost' password='fog13blik'")
except:
    print ("I am unable to connect to the database")
cur = conn.cursor()
cur.execute("""SELECT article.id, article.title as hash_name
                   FROM hash
                   INNER JOIN article_hash ON article_hash.hash = hash.id
                   INNER JOIN article ON article_hash.article = article.id
                   WHERE hash.name = """ + hash_tag + """ and article.data > """ + date_from + """
                                                   and article.data <""" + date_to)

rows = cur.fetchall()
for row in rows:
    print(row[0], row[1].strip())


conn.commit()

# SELECT article.id as article_id , article_hash.hash as hash_id, article_hash.article as article_id, hash.name as hash_name
# FROM article_hash
# INNER JOIN article ON article_hash.article = article.id
# INNER JOIN hash ON article_hash.hash = hash.id

# SELECT * FROM hash WHERE hash.name = '3d_graphics'

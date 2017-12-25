import datetime
import psycopg2
from psycopg2 import sql


def db_insert(datas_for_insert):

    id = datas_for_insert[0]
    type = datas_for_insert[1]
    title = datas_for_insert[2]
    author = datas_for_insert[3]
    data = datas_for_insert[4]
    hashes = datas_for_insert[5]

    try:
        conn = psycopg2.connect("dbname='fogstream_rubicon' user='vladislav' host='localhost' password='fog13blik'")
    except:
        print ("I am unable to connect to the database")
    cur = conn.cursor()

    # Проверяем, есть ли статья с таким id
    cur.execute("""SELECT "type" FROM "article" WHERE "id"='{}';""".format(id))
    if cur.fetchall():
        print('The article with same id alredy exist.')
    # Если нет, пытаемся добавить
    else:
        # Проверяем, есть ли автор с таким именем, и если есть получаем его id
        cur.execute("""SELECT "id" FROM "author" WHERE "name"='{}';""".format(author))
        rows = cur.fetchall()
        if rows:
            author_id = rows[0]
        # А если нет, добавляем и получаем его id
        else:
            cur.execute(
                sql.SQL("insert into {} (name)  values (%s)")
                    .format(sql.Identifier('author')),
                [author])
            cur.execute("""SELECT "id" FROM "author" WHERE "name"='{}';""".format(author))
            author_id = cur.fetchall()[0]

        # cur.execute("""SELECT "id" FROM "company" WHERE "name"='{}';""".format(company))
        # rows = cur.fetchall()
        # if rows:
        #     print('такая компания уже есть')
        #     company_id = rows[0]
        # else:
        #     cur.execute(
        #         sql.SQL("insert into {} (name)  values (%s)")
        #             .format(sql.Identifier('company')),
        #         [company])
        #     cur.execute("""SELECT "id" FROM "company" WHERE "name"='{}';""".format(company))
        #     company_id = cur.fetchall()[0]
    # Собственно добавляем статью
        cur.execute(
            sql.SQL("""insert into {} (id, type, author, title, data)  
                       values (%s, %s, %s, %s, %s)""")
                .format(sql.Identifier('article')),
            [id, type, author_id, title, data])

    for hash_name in hashes:
        hash_name = hash_name[:-1]
        cur.execute("""SELECT "id" FROM "hash" WHERE "name"='{}';""".format(hash_name))
        rows = cur.fetchall()
        if rows:
            # print('такой хэш(',hash_name ,':', rows[0],') уже есть')

            hash_id = rows[0]
        else:
            cur.execute(
                sql.SQL("insert into {} (name)  values (%s)")
                    .format(sql.Identifier('hash')),
                [hash_name])
            cur.execute("""SELECT "id" FROM "hash" WHERE "name"='{}';""".format(hash_name))
            hash_id = cur.fetchall()[0]
        cur.execute("""SELECT "article" FROM "article_hash" WHERE "article"='{}' AND "hash" = '{}';""".format(id, hash_id[0]))

        if not cur.fetchall():
            cur.execute(
                    sql.SQL("insert into {} (article, hash)  values (%s, %s)")
                        .format(sql.Identifier('article_hash')),
                    [id, hash_id])
        # else:
            # print('такое сочитание article', id, ' и hash', hash_id, ' уже есть')
    conn.commit()

datas_for_insert = ['344132', 'blog', 'Мастер-класс «Почему Стив Джобс любил шрифты» (Алексей Каптерев)', 'Olga_ol', datetime.datetime(2017, 12, 7, 16, 27), ['study/', 'typography/', 'graph_design/', 'mailru/']]
# db_insert(datas_for_insert)


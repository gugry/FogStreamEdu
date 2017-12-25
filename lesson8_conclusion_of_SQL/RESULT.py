import HabrPageParser
import db_insert
import all_id_pages

id_pages = all_id_pages.all_id_pages[:3]
id_pages = [['post', '344916'], ['post', '344600'], ['post', '344822']]
print(id_pages)

parced_pages = HabrPageParser.parse_page(id_pages)
for parced_page in parced_pages:
    print(parced_page)
    # db_insert.db_insert(parced_page)


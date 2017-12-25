from html.parser import HTMLParser
from read_site_content import read_site_content
import datetime
import all_id_pages

class HabrPageParser(HTMLParser):

    bull_title = False
    bull_user = False
    bull_hash = False
    bull_ul = False
    bull_data = False


    title=''
    user = ''
    data = []
    hash = []


    def handle_starttag(self, tag, attrs):
        if tag == 'ul':
            for attr in attrs:
                if attr[1] == 'post__hubs post__hubs_full-post inline-list':
                    self.bull_ul=True

        if tag == 'a':
            for index, attr in enumerate(attrs):
                if str(attr[1])[21:25] == 'hub/':
                    self.hash.append(str(attr[1])[25:])
                if str(attr[1]) == 'inline-list__item-link hub-link ':
                    if str(attrs[index - 1][1])[21:29] == 'company/':
                        self.hash.append(str(attrs[index - 1][1])[29:])
                        self.bull_ul = False

        if tag == 'span':
            for attr in attrs:
                if attr[1] == 'post__title-text':
                    self.bull_title = True
                if attr[1] == 'user-info__nickname user-info__nickname_small':
                    self.bull_user = True
                if attr[1] == 'post__time':
                    self.bull_data = True

    def handle_data(self, data):
        day=''
        month=''
        year=''
        time=''

        if self.bull_title:
            self.title = data
            self.bull_title = False

        if self.bull_user:
            self.user = data
            self.bull_user = False

        if self.bull_hash:
            self.hash = data
            self.bull_hash = False

        if self.bull_data:
            split = data.lstrip().split(' ')
            all_month = {'января':1, 'февраля':2, 'марта':3, 'апреля':4, 'мая':5, 'июня':6,
                         'июля':7, 'августа':8, 'сентября':9, 'октября':10, 'ноября':11,'декабря':12,}
            if split[0] == 'вчера' or split[0] == 'сегодня':
                date = datetime.datetime.today()
                yesterday_date = date - datetime.timedelta(days=1)
                all_date = {'вчера':yesterday_date.day, 'сегодня':date.day}
                day = all_date.get(split[0])
                month = date.month
            else:
                day = split[0]

                month = all_month.get(split[1])

            time =split[-1].split(':')

            if len(split) > 4:
                year = split[2]
            else:
                year = str(datetime.datetime.now()).split('-')[0]

            self.data = datetime.datetime(int(year), int(month), int(day), int(time[0]),int(time[1]))
            self.bull_data = False

    def clean_hash(self):
        self.hash = []


id_pages = all_id_pages.all_id_pages[:3]

print('id_pages ', id_pages )

def parse_page(id_pages):
    lenn = len(id_pages)
    parser = HabrPageParser()
    result=[]
    for index, id_page in enumerate(id_pages):
            print(index,'/',lenn)
            link = 'https://habrahabr.ru/post/' + id_page[1]
            habr_page = read_site_content(link)
            parser.feed(habr_page)
            id = id_page[1]
            type = id_page [0]
            title = parser.title
            author = parser.user
            hashes = parser.hash
            parser.clean_hash()
            data = parser.data
            result.append([id, type, title, author, data, hashes])
    return result



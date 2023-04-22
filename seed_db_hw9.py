import mongoengine
import json
import pymongo

from models import Authors, Quotes


def seeds_db():
    with open('authors.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        for i in data:
            author = Authors(fullname=i.get('fullname'),
                             born_date=i.get('born_date'),
                             born_location=i.get('born_location'),
                             bio=i.get('bio')) \
                .save()

    with open('quotes.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        for i in data:
            author = Authors.objects(fullname=i.get('author', None)).first()
            quote = Quotes(tags=i.get('tags'),
                           author=author,
                           quote=i.get('quote')) \
                .save()






if __name__ == '__main__':
    seeds_db()
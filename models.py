from mongoengine import connect, Document, StringField, ListField, ReferenceField
from pathlib import Path
import configparser

# file_config = Path(__file__).parent.parent.joinpath('config.ini')
config = configparser.ConfigParser()
config.read('config.ini')

mongo_user = config.get('DEV_DB', 'USER')
mongodb_pass = config.get('DEV_DB', 'PASSWORD')
domain = config.get('DEV_DB', 'DOMAIN')
# port = config.get('DEV_DB', 'PORT')
db_name = config.get('DEV_DB', 'DB_NAME')


# connect(host="mongodb://localhost:27017/web10")
# client = MongoClient("mongodb+srv://userweb10:567234@cluster0.eukkmyr.mongodb.net/
# ?retryWrites=true&w=majority",
#                      server_api=ServerApi('1'))
connect(host=f"""mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority""", ssl=True)


class Authors(Document):
    fullname = StringField(max_length=70)
    date_born = StringField(max_length=50)
    born_location = StringField(max_length=150)
    bio = StringField()


class Quotes(Document):
    tags = ListField(StringField())
    author = ReferenceField(Authors)
    quote = StringField()

from peewee import (CharField,
                    SqliteDatabase,
                    Model,
                    TextField,
                    DateTimeField,
                    IntegrityError)
import datetime
db = SqliteDatabase("blogs.db")

blogs = [
    {'title': 'A new entry', 'body': 'This is a body'},
    {'title': 'Another entry', 'body': 'A post body'}
]


class Blog(Model):
    title = CharField(default='title', max_length=255, unique=True)
    body = TextField(default='A post body')
    entrytime = DateTimeField(default=datetime.datetime.now)

    @classmethod
    def add(cls, title, body):
        try:
            Blog.create(
                title=title,
                body=body
            )
        except IntegrityError:
            pass

    @classmethod
    def list(cls):
        initialize()
        blogs = Blog.select()
        return blogs


    class Meta:
        database = db


def initialize():
    db.create_tables([Blog], safe=True)
    for blog in blogs:
        try:
            Blog.create(
                title=blog.get('title'),
                body=blog.get('body')
            )
        except IntegrityError:
            pass

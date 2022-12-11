from peewee import *
from datetime import datetime
from decouple import config

database = MySQLDatabase(config('MYSQL_DB'),
                       user=config('MYSQL_USER'), 
                       password=config('MYSQL_PASSWORD'), 
                       host=config('MYSQL_HOST'), 
                       port=int(config('MYSQL_PORT')))
class User(Model):
    username = CharField(max_length=50, unique=True)
    password = CharField(max_length=50)
    created_at = DateTimeField(default=datetime.now)

    def __str__(self):
        return self.username

    class Meta:
        database = database
        table_name = 'users'

class Movie(Model):
    title = CharField(max_length=50)
    created_at = DateTimeField(datetime.now)

    def __str__(self):
        return self.title

    class Meta:
        database = database
        table_name = 'movies'


class UserReview(Model):
    user = ForeignKeyField(User, backref='reviews')
    movie = ForeignKeyField(Movie, backref='reviews')
    review = TextField()
    score = IntegerField()
    created_at = DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.user.username} - {self.movie.title}'

    class Meta:
        database = database
        table_name = 'users_reviews'




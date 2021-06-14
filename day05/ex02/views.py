from django.conf import settings
from django.http import HttpRequest, HttpResponse
import psycopg2
from django.shortcuts import render


def Movies(request: HttpRequest()):
    try:
        conn = psycopg2.connect("dbname={} user={} password={} host={} port={}".format(
            settings.DATABASES['default']['NAME'],
            settings.DATABASES['default']['USER'],
            settings.DATABASES['default']['PASSWORD'],
            settings.DATABASES['default']['HOST'],
            settings.DATABASES['default']['PORT']))

        SQL1 = """CREATE TABLE IF NOT EXISTS ex02_movies (
            title char(64) UNIQUE NOT NULL,
            episode_nb INT PRIMARY KEY,
            opening_crawl TEXT,
            director VARCHAR(32) NOT NULL,
            producer VARCHAR(128) NOT NULL,
            release_date DATE NOT NULL
            );"""

        with conn.cursor() as curs:
            curs.execute(SQL1)
            curs.execute('COMMIT')
        return HttpResponse("OK")

    except Exception as e:
        return HttpResponse(e)


def Movies_insert(request: HttpRequest()):
    
    try:
        conn = psycopg2.connect("dbname={} user={} password={} host={} port={}".format(
            settings.DATABASES['default']['NAME'],
            settings.DATABASES['default']['USER'],
            settings.DATABASES['default']['PASSWORD'],
            settings.DATABASES['default']['HOST'],
            settings.DATABASES['default']['PORT']))
        movies = [
        {
            "episode_nb": 1,
            "title": "The Phantom Menace",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "1999-05-19"
        },
        {
            "episode_nb": 2,
            "title": "Attack of the Clones",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "2002-05-16"
        },
        {
            "episode_nb": 3,
            "title": "Revenge of the Sith",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "2005-05-19"
        },
        {
            "episode_nb": 4,
            "title": "A New Hope",
            "director": "George Lucas",
            "producer": "Gary Kurtz, Rick McCallum",
            "release_date": "1977-05-25"
        },
        {
            "episode_nb": 5,
            "title": "The Empire Strikes Back",
            "director": "Irvin Kershner",
            "producer": "Gary Kurtz, Rick McCallum",
            "release_date": "1980-05-17"
        },
        {
            "episode_nb": 6,
            "title": "Return of the Jedi",
            "director": "Richard Marquand",
            "producer": "Howard G. Kazanjian, George Lucas, Rick McCallum",
            "release_date": "1983-05-25"
        },
        {
            "episode_nb": 7,
            "title": "The Force Awakens",
            "director": "J. J. Abrams",
            "producer": "Kathleen Kennedy, J. J. Abrams, Bryan Burk",
            "release_date": "2015-12-11"
        }
        ]
        result= []
        with conn.cursor() as curs:
            for movie in movies:
                try:
                # SQL2 = """INSERT INTO ex02_movies(title, episode_nb, director, producer, release_date)
                    curs.execute("""insert into %s(title, episode_nb, director, producer, release_date) 
                    values (%%s, %%s, %%s, %%s, %%s)""" % 'ex02_movies',
                    [movie['title'], movie['episode_nb'], movie['director'], movie['producer'], movie['release_date']])
                    result.append("{} - OK<br>".format(movie['title'] ))
                    conn.commit()
                except psycopg2.DatabaseError as e:
                    conn.rollback()
                    result.append(e)
                    result.append("<br>")
                # curs.execute('COMMIT')
        return HttpResponse(result)

    except Exception as e:
        print(HttpRequest())
        return HttpResponse(e)

def display(request):
    try:
        conn = psycopg2.connect("dbname={} user={} password={} host={} port={}".format(
                settings.DATABASES['default']['NAME'],
                settings.DATABASES['default']['USER'],
                settings.DATABASES['default']['PASSWORD'],
                settings.DATABASES['default']['HOST'],
                settings.DATABASES['default']['PORT']))
        # SQL = "select * from ex02_movies"
        with conn.cursor() as curs:
            curs.execute("""select * from ex02_movies""")
            movies = curs.fetchall()

        return render(request, 'display.html', { "movies" : movies})
    # except psycopg2.DataError as e:
    #     return HttpResponse(e)
    except Exception as e:
        return HttpResponse("No data available")

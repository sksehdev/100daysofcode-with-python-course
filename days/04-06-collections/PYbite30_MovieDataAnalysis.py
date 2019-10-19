import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve
import json

BASE_URL = 'http://projects.bobbelderbos.com/pcc/movies/'
TMP = '/tmp'

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    with open(TMP + '/' + fname,newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        directorWithMovies = defaultdict(list)
        for row in csv_reader:
            Movie = namedtuple("Movie","title , year , score")
            if row["title_year"] != "" and int(row["title_year"]) > MIN_YEAR:
                m = Movie(title = row["movie_title"],year = row["title_year"],score = row["imdb_score"])
                directorWithMovies[row["director_name"]].append(m)
    #print(json.dumps(directorWithMovies, indent=2))
    return directorWithMovies
    pass


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    imdb_score_list = []
    for i in movies :
        imdb_score_list.append(float(i.score))
    #print(imdb_score_list)
    mean_imdb_score = sum(imdb_score_list) / len(imdb_score_list)
    #print(round(mean_imdb_score,1))
    return round(mean_imdb_score,1)
    pass


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    average_scores = []
    for key , value in directors.items():
        director = namedtuple("director", "name, score")
        if len(directors[key]) >= MIN_MOVIES:
            d = director(name = key , score = calc_mean_score(value))
            average_scores.append(d)
    average_score1 = sorted(average_scores,key=lambda x: x.score,reverse=True)
    print(average_score1)
    pass

director_movies = get_movies_by_director()


#movies_sergio = director_movies['Sergio Leone']
#print(movies_sergio)

#calc_mean_score(movies_sergio)

get_average_scores(director_movies)
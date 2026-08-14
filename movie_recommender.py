import requests
import random

url = "https://raw.githubusercontent.com/erik-sytnyk/movies-list/master/db.json"

response = requests.get(url)

data = response.json()

movies = data["movies"]

genre = input("Enter a genre: ")

matching_movies = []

for movie in movies:
    if genre.lower() in [g.lower() for g in movie["genres"]]:
        matching_movies.append(movie)

if matching_movies:
    movie = random.choice(matching_movies)

    print("\n🎬 Movie Recommendation")
    print("Title:", movie["title"])
    print("Year:", movie["year"])
    print("Genres:", movie["genres"])

else:
    print("Sorry, no movies found for that genre.")
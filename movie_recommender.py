import requests
import random

url = "https://raw.githubusercontent.com/erik-sytnyk/movies-list/master/db.json"

response = requests.get(url)

movies = response.json()

movie = random.choice(movies["movies"])

print("🎬 Movie Recommendation")
print()
print("Title:", movie["title"])
print("Year:", movie["year"])
print("Genres:", movie["genres"])
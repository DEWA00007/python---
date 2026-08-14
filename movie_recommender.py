import requests
import random

url = "https://raw.githubusercontent.com/erik-sytnyk/movies-list/master/db.json"

response = requests.get(url)
data = response.json()

movies = data["movies"]

print("🎬 MOVIE RECOMMENDER")
print()
print("Choose a genre:")
print("1. Action")
print("2. Comedy")
print("3. Drama")
print("4. Horror")
print("5. Romance")
print("6. Sci-Fi")

choice = input("\nEnter your choice: ")

genres = {
    "1": "Action",
    "2": "Comedy",
    "3": "Drama",
    "4": "Horror",
    "5": "Romance",
    "6": "Sci-Fi"
}

if choice in genres:
    selected_genre = genres[choice]

    matching_movies = []

    for movie in movies:
        if selected_genre.lower() in [g.lower() for g in movie["genres"]]:
            matching_movies.append(movie)

    if matching_movies:
        movie = random.choice(matching_movies)

        print("\n🍿 Your recommendation:")
        print("Title:", movie["title"])
        print("Year:", movie["year"])
        print("Genres:", movie["genres"])

    else:
        print("Sorry, no movies found.")

else:
    print("❌ Invalid choice.")
# My favorite movies and their release years
favorite_movies = [
    {"name": "The Lion King", "year": 1994},
    {"name": "Titanic", "year": 1997},
    {"name": "The Dark Knight", "year": 2008},
    {"name": "Black Panther", "year": 2018},
    {"name": "Spider-Man: No Way Home", "year": 2021}
]

# Function to check when a movie was released
def check_movie(movie):
    if movie["year"] < 2000:
        print("This movie was released before 2000")
    else:
        print("This movie was released after 2000")
        return movie["name"]


# Empty list for recent movies
recent_movies = []

# Check each movie using a loop
for movie in favorite_movies:
    result = check_movie(movie)

    if result is not None:
        recent_movies.append(result)

# Print the recent movies
print("Recent movies:", recent_movies)
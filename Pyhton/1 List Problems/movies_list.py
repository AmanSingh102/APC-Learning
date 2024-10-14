listOfMovie = []
for i in range(0,3):
    movie = input(f"Enter {i+1} Movie name : ")
    listOfMovie.append(movie)

print("List of movie are :-",listOfMovie)


listOfMovies = [""] * 3
for i in range(0,3):
    listOfMovies[i] = input(f"Enter {i+1} Movie name : ")

print("List of movie are :-",listOfMovies)
current_movie = { 'The Grinch' : '11:00am',
                    'Rudolph' : ' 1:00 pm',
                    'Frosty the Snowman' : '3:00pm',
                    'Christmas Vacation' : '5:00pm'}

print("We're currently showing the following movies:")
for key in current_movie:
    print(key)
movie = input('What movie would you like the showtime for?\n')

showtime = current_movie.get(movie)

if showtime == None:
    print("Requested showtime isn't available")
else:
    print(movie, 'is playing at',showtime)
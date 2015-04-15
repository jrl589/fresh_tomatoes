import media #import the file media.py in this directory
import fresh_tomatoes #import the file fresh_tomatoes.py

# Create instances of media.Movie class for some movies (not necessarily my favorites)
# 	-A Clockwork Orange
# 	-Pulp Fiction
# 	-Inglorious Basterds
# 	-Reservoir Dogs
# 	-Inception
# 	-The Godfather
#	-Fight Club
#	-Schingler's List
#	-The Lord of the Rings: Fellowship of the Ring
#
# media.Movie constructor takes four arguments (title, description, posterURL, trailerURL)


aClockworkOrange = media.Movie ( 
	'A Clockwork Orange' 
,	'In future Britain, charismatic delinquent Alex DeLarge is jailed and volunteers for an experimental aversion therapy developed by the government in an effort to solve society\'s crime problem - but not all goes according to plan.'
, 	'http://www.collativelearning.com/PICS%20FOR%20WEBSITE/ACO%20expanded/posters/clockwork.jpg'
, 'https://www.youtube.com/watch?v=xHFPi_3kc1U' )

pulpFiction	= media.Movie (
	'Pulp Fiction'
, 	'The lives of two mob hit men, a boxer, a gangster\'s wife, and a pair of diner bandits intertwine in four tales of violence and redemption.'
, 	'http://vignette3.wikia.nocookie.net/pulp-fiction/images/5/5e/Pulpy_Fiction_Poster.jpg/revision/latest?cb=20100421131653'
, 	'https://www.youtube.com/watch?v=s7EdQ4FqbhY' )

inglouriousBasterds = media.Movie (
	'Inglourious Basterds'
,	'In Nazi-occupied France during World War II, a plan to assassinate Nazi leaders by a group of Jewish U.S. soldiers coincides with a theatre owner\'s vengeful plans for the same.'
, 	'http://upload.wikimedia.org/wikipedia/en/c/c3/Inglourious_Basterds_poster.jpg'
, 	'https://www.youtube.com/watch?v=KnrRy6kSFF0' )

reservoirDogs = media.Movie (
	'Reservoir Dogs'
, 	'After a simple jewelery heist goes terribly wrong, the surviving criminals begin to suspect that one of them is a police informant.'
, 	'http://images.moviepostershop.com/reservoir-dogs-movie-poster-1992-1020470548.jpg'
, 	'https://www.youtube.com/watch?v=vayksn4Y93A' )

inception = media.Movie (
	'Inception'
, 	'A thief who steals corporate secrets through use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.'
, 	'http://www.taramagazine.com/wp-content/uploads/2013/09/inception-movie-poster-themed-wedding-reception-invitation.jpg'
,	'https://www.youtube.com/watch?v=8hP9D6kZseM' )

theGodfather = media.Movie (
	'The Godfather'
, 	'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.'
, 	'http://fontmeme.com/images/The-Godfather-Poster.jpg'
, 	'https://www.youtube.com/watch?v=5DO-nDW43Ik' )

fightClub = media.Movie (
	'Fight Club'
, 	'An insomniac office worker looking for a way to change his life crosses paths with a devil-may-care soap maker and they form an underground fight club that evolves into something much, much more...'
, 	'http://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg'
, 	'https://www.youtube.com/watch?v=_XgQA9Ab0Gw' )

schindlersList = media.Movie (
	'Schindler\'s List'
, 	'In Poland during World War II, Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution by the Nazis.'
, 	'http://onlain-torrent-filmi.net/uploads/posts/2014-04/1398323829_586480724_posters_torrent.jpg'
, 	'https://www.youtube.com/watch?v=gG22XNhtnoY' )

theFellowshipOfTheRing = media.Movie (
	'The Lord of the Rings: The Fellowship of the Ring'
, 	'A meek hobbit of the Shire and eight companions set out on a journey to Mount Doom to destroy the One Ring and the dark lord Sauron.'
, 	'https://www.movieposter.com/posters/archive/main/105/MPW-52979'
, 	'https://www.youtube.com/watch?v=V75dMMIW2B4' )


#Add Movie instances to an array
movies = [

	aClockworkOrange,
	pulpFiction,
	inglouriousBasterds,
	reservoirDogs,
	inception,
	theGodfather,
	fightClub,
	schindlersList,
	theFellowshipOfTheRing

]

#Pass movies array to fresh_tomatoes.open_movies_page
#
#fresh_tomatoes.open_movies_page parses the movie information into html and
#creates a file with that html which is then opened in your default browser
fresh_tomatoes.open_movies_page ( movies )


import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "Woody, Buzz, and the gang star in the hilarious fantasy-adventure about the lives Andy's toys lead when they're left alone.","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://youtu.be/KYz2wyBy3kc")

avatar = media.Movie("Avatar","A marine on an alien planet", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")

star_wars = media.Movie("Attack of the Clones", "Star Wars enters the clone wars to establish peace", "https://upload.wikimedia.org/wikipedia/en/3/32/Star_Wars_-_Episode_II_Attack_of_the_Clones_%28movie_poster%29.jpg", "https://www.youtube.com/watch?v=9C-fZCLsISA")

new_groove = media.Movie("The Emperor's New Groove", "A young emperor gets changed into a llama and has adventures", "http://www.gstatic.com/tv/thumb/movieposters/26687/p26687_p_v8_ae.jpg", "https://www.youtube.com/watch?v=ppYOZ4eFU2M")

inside_out = media.Movie("Inside Out", "Go inside the mind of a young girl with all her emotions", "http://t0.gstatic.com/images?q=tbn:ANd9GcTtZdvrahQxfjGkSBJCS-uiZKUfJNH4ddsqgCbV5oFkQiQ-tszE", "https://www.youtube.com/watch?v=_MC3XuMvsDI")

zootopia = media.Movie("Zootopia", "A city of animals needs good cops", "http://t2.gstatic.com/images?q=tbn:ANd9GcQj1fU0-Idujcrs_MB2xEWbVEygeCkcjYUp4Z-hSIPqgu0vFbQi", "https://www.youtube.com/watch?v=bY73vFGhSVk")

#print(toy_story.poster_image_url)
#show trailer
#toy_story.show_trailer()
movies = [toy_story, avatar, star_wars, new_groove, inside_out, zootopia]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__module__) # Prints the name of the module in which this class was defined.
#print(media.Movie.__name__)   # Prints the name of the class
#print(media.Movie.__doc__)    # Prints the documation

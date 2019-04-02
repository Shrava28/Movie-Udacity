import fresh_tomatoes
import media

Shawshank_Redemption = media.Movie(
    "Shawshank Redemption", 
    "Brilliant Banker of Jail !!", 
    "https://i.pinimg.com/236x/70/ed/b4/70edb4853ec8a3988aecd084317d7cb4.jpg", 
    "https://youtu.be/6hB3S9bIaco",
    )
# print(Shawshank_Redemption.storyline)
# Shawshank_Redemption = Shawshank_Redemption.strip()

Captain_Marvel = media.Movie(
    "Captain Marvel", 
    "Captain of Avengers with extraordinary power", 
    "https://i.ytimg.com/vi/0LHxvxdRnYc/sddefault.jpg#404_is_fine", 
    "https://youtu.be/Z1BCujX3pw8",
    )
# print(Captain_Marvel.storyline)

Batman_Dark_Knight_Rises = media.Movie(
    "Batman : Dark Knight Rises", 
    "A defender of justice !!!", 
    "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg", 
    "https://youtu.be/GokKUqLcvD8",
    )
# print(Batman_Dark_Knight_Rises.storyline)

Thor_Ragnarok = media.Movie(
    "Thor Ragnarok", 
    "A Story of a Goddess of Death !", 
    "https://i.pinimg.com/236x/68/d0/d2/68d0d2b4caa030fb91005c7076282b60.jpg", 
    "https://youtu.be/ue80QwXMRHg",
    )
# print(Thor_Ragnarok.storyline)

Interstellar = media.Movie(
    "Interstellar", 
    "A Story about Fifth Dimension !!", 
    "https://i.ebayimg.com/images/g/GtUAAOxycmBStD9p/s-l300.jpg", 
    "https://youtu.be/zSWdZVtXT7E",
    )
# print(Interstellar.storyline)

Persuit_of_Happyness = media.Movie(
    "Persuit of Happyness", 
    "Evicted Father becomes Millionaire!!!", 
    "https://wallpapercave.com/wp/wp2618500.jpg", 
    "https://youtu.be/89Kq8SDyvfg",
    )
# print(Persuit_of_Happyness.storyline)

movies = [
    Shawshank_Redemption, Captain_Marvel, Batman_Dark_Knight_Rises, 
    Thor_Ragnarok, Interstellar, Persuit_of_Happyness
    ]
fresh_tomatoes.open_movies_page(movies)
print (media.Movie.valid_ratings)
# to print class name : 
print(media.Movie.__name__)
# to print class doc :
print(media.Movie.__doc__)
# to print module name :
print(media.Movie.__module__)

import fresh_tomatoes
import media

# Toy Story movie: movie title, storyline, poster image and movie trailer
toy_story = media.Movie(
                        "Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "toystory.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# Avatar movie: movie title, storyline, poster image and movie trailer
avatar = media.Movie("Avatar", "A marine on an Alien planet",
                     "avatar.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# Harry Potter movie: movie title, storyline, poster image and movie trailer
harry_potter = media.Movie(
                          "Harry Potter",
                          """A young boy with a great destiny proves his worth while attending Hogwarts\
School of Witchcraft and Wizardry.""",
                          "hp.jpg",
                          "https://www.youtube.com/watch?v=fcPYNxGM7BA")

# Inception movie: movie title, storyline, poster image and movie trailer
inception = media.Movie(
                      "Inception",
                      """A skilled extractor is offered a chance to regain his\
old life as payment for a\
task considered to be impossible.""",
                      "i.jpg",
                      "https://www.youtube.com/watch?v=8hP9D6kZseM")

# YehJawaniHaiDeewanimovie:movie title,storyline,poster image and movie trailer
yeh_jawani_hai_deewani = media.Movie(
                            "Yeh Jawaani Hai Deewani",
                            """Kabir and Naina bond during a trekking trip\
Before Naina can express herself,\
Kabir leaves India to pursue his career\
They meet again years later, but he still\
cherishes his dreams more than bonds.""",
                            "yjhd.jpg",
                            "https://www.youtube.com\/watch?v=Rbp2XUSeUNE")

# Fast and Furious movie: movie title,storyline, poster image and movie trailer
fast_and_furious = media.Movie(
                                "Fast and Furious",
                                """An undercover cop infiltrates the world of\
street racing to solve a series of truck
hijackings perpetrated by Dominic Toretto""",
                                "ff.jpg",
                                "https://www.youtube.com/watch?v=ZsJz2TJAPjw")
movies = [
          toy_story, avatar, harry_potter,
          inception, yeh_jawani_hai_deewani, fast_and_furious]
fresh_tomatoes.open_movies_page(movies)

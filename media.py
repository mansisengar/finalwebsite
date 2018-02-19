import webbrowser
# imports the webbrowswer function from the library so it can be used


class Movie():
    # creates objects for every movie
    __name__ = "website"

    def __init__(
                self, movie_title, movie_storyline,
                poster_image, trailer_youtube):
                    self.title = movie_title
                    self.storyline = movie_storyline
                    self.poster_image_url = poster_image
                    self.trailer_youtube_url = trailer_youtube
# init initializes value.

    def show_trailer(self):
        # opens web browser and plays the trailer
        webbrowser.open(self.trailer_youtube_url)

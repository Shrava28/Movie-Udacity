import webbrowser


class Movie():
    """This class provides a way to store movie related information"""
    # This class provides a way to store movie related information
    # title
    # story line
    # reviews
    # poster
    # trailer link
    valid_ratings = ["G", "PG", "PG-13", "R"]

    def __init__(
            self, movie_title, movie_storyline, poster_image, 
            trailer_youtube):
        """ This docstring should explain constructor methods input
            and output

            :param movie_title: string
            :param movie_storyline: string
            :param poster_image: string
            :param trailer_youtube: string
        """            
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ This docstring should explain what the show_trailer
            function does
            input and output
        """
        webbrowser.open(self.trailer_youtube_url)

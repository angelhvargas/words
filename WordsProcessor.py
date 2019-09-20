from WikiPage import WikiPage
import os


class WordsProcessor:
    """
    class WordsProcessor does count words in a given file using
    map-reduce approach
    """
    file = None

    def __init__(self, data):
        if isinstance(data, WikiPage):
            pass
        elif isinstance(data, str):
            if os.path.isfile(data):
                self.file = data
            else:
                raise FileExistsError("Invalid file or path")

    def load_data(self):
        pass
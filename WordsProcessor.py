import mmap
import os


class WordsProcessor:
    """class WordsProcessor does count words in a given file using
    map-reduce approach"""

    file_path = None

    def __init__(self, file_path):
        self.file_path = file_path
        assert os.path.exists(self.file_path)

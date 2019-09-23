import os
import re

from WikiPage import WikiPage
from collections import defaultdict


class WordsProcessor:
    """
    class WordsProcessor does count words in a given file using
    map-reduce approach
    """

    def __init__(self):
        self._file = None
        self._text = None
        self._map = defaultdict(int)
        self._words = defaultdict(int)

    def load_data(self, __data):
        """
        Load dto or file to be processed
        :param __data:
        :return: self
        """
        if isinstance(__data, WikiPage):
            self._text = __data.extract
            _filename = str(__data.page_id)+'.txt'
            self.write_in_file(_filename)
            self.file = _filename

        elif isinstance(__data, str) and os.path.isfile(__data):
            self.file = __data
        else:
            raise FileExistsError("Invalid file or path, a valid dto or file is required")
        return self

    def write_in_file(self, __filename="text.txt"):
        """write_in_file

        writes page extract to a file, this allow to flush requests to files if needed in case of
         parallel processing.
        :param __filename: str
        :return: self|False
        """
        try:
            with open(__filename, 'w+', encoding="latin-1", errors='ignore') as writer:
                writer.write(self.text)
                writer.close()
            return self
        except FileExistsError("can't write file to filesystem"):
            return False

    @staticmethod
    def map(__text) -> list:
        """
        from a given string, splits 4 characters or larger words into a list
        :param __text: string
        :return: list
        """
        pattern = re.compile(r"(\w{4,})")
        words_list = pattern.findall(__text.lower())
        return words_list

    def reduce(self, __map) -> dict:
        """
        reduce mapped dictionary to count repeated values
        :param __map:
        :return: dict
        """
        for word in __map:
            self._words[word] += 1
        return self.words

    def process(self) -> defaultdict:
        """
        process map reduce to a valid loaded file.
        :return: defaultdict
        """
        if isinstance(self.file, str):
            try:
                with open(self.file) as fr:
                    line = fr.readline()
                    while 1:
                        line = fr.readline()
                        _map = self.map(line)
                        self.reduce(_map)
                        if not line:
                            break

            except FileExistsError as e:
                raise e
        elif isinstance(self.text, str):
            _map = WordsProcessor.map(self.text)
            self.reduce(_map)
        return self.words

    @property
    def text(self):
        return self._text

    @property
    def file(self):
        return self._file

    @property
    def words(self):
        return self._words

    @words.setter
    def words(self, _words):
        self._words = _words

    @text.setter
    def text(self, _text):
        self._text = _text

    @file.setter
    def file(self, _file):
        self._file = _file
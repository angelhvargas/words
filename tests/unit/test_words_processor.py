from WordsProcessor import WordsProcessor
from WikiPage import WikiPage
import pytest


@pytest.fixture(scope="class")
def test_file():
    return 'test_file.txt'


@pytest.fixture(scope="class")
def wiki_page():
    wiki_page = WikiPage(
        page_id=1234,
        title="this title",
        extract="test!! text text lazy fox is coming from a fox mom.$^\n"
    )
    return wiki_page


@pytest.fixture(scope="class")
def words_processor():
    words_processor = WordsProcessor()
    return words_processor


@pytest.mark.usefixtures("wiki_page", "words_processor", "test_file")
class TestWordsProcessor:

    def test_can_instantiate_words_processor(self, wiki_page: WikiPage, words_processor: WordsProcessor) -> None:
        """
        test if WordsProcessor class does exists
        or can be instantiate

        :param wiki_page:
        :param words_processor:
        :return: None
        """
        # valid file
        assert isinstance(words_processor, WordsProcessor)

    def test_can_load_data_from_dto(self, wiki_page: WikiPage, words_processor: WordsProcessor) -> None:
        """
        test if the class can load data from a compatible dto
        :param wiki_page:
        :param words_processor:
        :return: None
        """
        assert words_processor.load_data(wiki_page).text == "test!! text text lazy fox is coming from a fox mom.$^\n"

    def test_can_load_file(self, words_processor: WordsProcessor, test_file: str):
        """
        test if class WordsProcessor can load and read a file line
        :param words_processor:
        :return: None
        """

        assert words_processor.load_data(test_file)
        with pytest.raises(FileExistsError):
            words_processor.load_data("random_file_not_exists.txt")

    def test_can_write_data_to_file(self, words_processor: WordsProcessor, wiki_page: WikiPage):
        """
        test if can write out data loaded from a passed dto
        :param words_processor:
        :param wiki_page:
        :return: None
        """
        words_processor.load_data(wiki_page)
        assert words_processor.write_in_file("test_file.txt")

    def test_can_map_words(self, words_processor: WordsProcessor, wiki_page: WikiPage):
        """
        test word mapping, if words are 4 characters or more
        :param words_processor:
        :param wiki_page:
        :return: None
        """
        assert words_processor.map(wiki_page.extract) == ["test", "text", "text", "lazy", "coming", "from"]

    def test_can_reduce_map(self, words_processor: WordsProcessor, wiki_page: WikiPage):
        """
        test to reduce a map and validates the output can be manipulated as a dictionary
        :param words_processor:
        :param wiki_page:
        :return: None
        """
        _map = words_processor.map(wiki_page.extract)
        words = words_processor.reduce(_map)
        # is as valid dict
        assert isinstance(dict(words), dict)
        # expected output assertion
        assert words == {'test': 1, 'text': 2, 'lazy': 1, 'coming': 1, 'from': 1}
        # expected output can be sorted descending
        assert dict(sorted(words.items(), key=lambda x: x[1], reverse=True)) == {'text': 2, 'test': 1, 'lazy': 1,
                                                                                 'coming': 1, 'from': 1}

    def test_can_map_reduce_from_file(self, words_processor: WordsProcessor, test_file: str):
        """
        test map-reduce process from a given file
        :param words_processor:
        :param test_file:
        :return: None
        """
        words_processor.load_data(test_file)
        result = words_processor.process()
        assert dict(sorted(result.items(), key=lambda x: x[1], reverse=True)) == {'text': 2, 'test': 1, 'lazy': 1,
                                                                                  'coming': 1, 'from': 1}
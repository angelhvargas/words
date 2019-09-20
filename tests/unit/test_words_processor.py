from WordsProcessor import WordsProcessor
from WikiPage import WikiPage
import pytest


@pytest.fixture(scope="module")
def wiki_page():
    wiki_page = WikiPage(page_id=1234, title="this title", extract="test text")
    return wiki_page


@pytest.fixture(scope="module")
def words_processor():
    words_processor = WordsProcessor('test.txt')
    return words_processor


@pytest.mark.usefixtures("wiki_page", "words_processor")
class TestWordsProcessor:

    def test_can_instantiate_words_processor(self, wiki_page, words_processor):
        """test if WordsProcessor class does exists
        or can be instantiate"""
        # valid file
        assert isinstance(words_processor, WordsProcessor)

        # invalid file
        with pytest.raises(FileExistsError):
            assert WordsProcessor('random_file')

        # valid wikipage dto
        assert WordsProcessor(wiki_page)

    def test_can_load_data_from_dto(self, wiki_page, words_processor):
        """
        :param wiki_page:
        :return:
        """
        words_processor.load_data()


from WordsProcessor import WordsProcessor
from WikiAPIClient import WikiAPIClient
from WikiPage import WikiPage
import pytest


@pytest.fixture(scope="class")
def test_file():
    return 'test_file.txt'


@pytest.fixture(scope="class")
def wikipedia_page_id():
    return '21721040'


@pytest.fixture(scope="class")
def wiki_api_client():
    wiki_api_client = WikiAPIClient()
    return wiki_api_client


@pytest.fixture(scope="class")
def words_processor():
    words_processor = WordsProcessor()
    return words_processor


@pytest.mark.usefixtures("wikipedia_page_id", "words_processor", "wiki_api_client")
class TestWordsProcessing:

    def test_can_map_reduce_from_wikipedia(self, wiki_api_client, wikipedia_page_id, words_processor):
        wiki_page_dto = wiki_api_client.get_wiki_page_extract(wikipedia_page_id)

        # check for a valid dto
        assert isinstance(wiki_page_dto, WikiPage)

        # check dto extract attribute is a string
        _extract = wiki_page_dto.extract
        assert isinstance(_extract, str)

        # check to load data from dto, and then if has created the temporary fie
        words_processor.load_data(wiki_page_dto)
        assert words_processor.file == wiki_page_dto.page_id+".txt"

        # valid data processing
        words = words_processor.process()
        assert isinstance(words, dict)






from WikiAPIClient import WikiAPIClient
from WikiPage import WikiPage
from pytest import *


@fixture(scope="class")
def api_client():
    api_client = WikiAPIClient()
    return api_client


@mark.usefixtures("api_client")
class TestWikiFetcher:

    valid_page_id_test = 21721040
    invalid_page_id_test = 21721234234124

    valid_endpoint = "https://en.wikipedia.org/w/api.php"

    invalid_endpoint = "https://en.wikipedia.org/w/api.phpw"

    valid_test_params = {
        "action": "query",
        "prop": "extracts",
        "pageids": valid_page_id_test,
        "explaintext": 1,
        "format": "json"
    }

    invalid_test_params = {
        "baz": "foo",
        "zoo": "fox",
        "pageids": valid_page_id_test,
        "text": 1,
        "format": "yaml"
    }

    def test_api_call(self, api_client):

        api_call = api_client.api_request(self.invalid_endpoint, self.valid_test_params)

        assert "error" in api_call.keys()

    def test_wikipedia_api_request_page_extract(self, api_client):
        """"""
        assert isinstance(api_client.get_wiki_page_extract(self.valid_page_id_test), WikiPage)
        assert not isinstance(api_client.get_wiki_page_extract(self.invalid_page_id_test), WikiPage)

    # def test_wikipedia_page_extract_written_to_file(self):
    #     """test if data pulled from wikipedia can be
    #      written in a file"""
    #     fetcher = WikiAPIClient()
    #     fetcher.get_wiki_page_extract(self.page_id_test)
    #     path = fetcher.to_file("test.txt")
    #     file = Path(path)
    #     assert file.is_file() is True
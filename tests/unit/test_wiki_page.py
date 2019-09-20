from WikiPage import WikiPage
import pytest


@pytest.fixture(scope="class")
def wiki_page():
    wiki_page = WikiPage(page_id=1234, title="this title", extract="test text")
    return wiki_page


@pytest.mark.usefixtures("wiki_page")
class TestWikiPageExtract:

    def test_can_instantiate_wiki_page_extract(self, wiki_page):
        """"""
        wiki_page_extract = wiki_page

        # test getters
        assert str(wiki_page_extract.title)
        assert str(wiki_page_extract.extract)
        assert int(wiki_page_extract.page_id)

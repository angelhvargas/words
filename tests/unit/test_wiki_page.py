from WikiPage import WikiPage


class TestWikiPageExtract:

    def test_can_instantiate_wiki_page_extract(self):
        """"""
        wiki_page_extract = WikiPage(page_id=1234, title="this title", extract="test text")
        assert str(wiki_page_extract.title)


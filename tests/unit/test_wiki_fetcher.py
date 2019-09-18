from WikiFetcher import WikiFetcher
from pathlib import Path


class TestWikiFetcher:

    page_id_test = 21721040

    def test_can_write_to_file_wikipedia_page_extract(self):
        """test if data pulled from wikipedia can be
         written in a file"""
        fetcher = WikiFetcher()
        fetcher.fetch_wiki_extract(self.page_id_test)
        path = fetcher.to_file("test.txt")
        file = Path(path)
        assert file.is_file() is True

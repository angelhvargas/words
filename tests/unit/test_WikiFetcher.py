from WikiFetcher import WikiFetcher
from pathlib import Path

page_id_test = 21721040


def test_can_write_to_file_wikipedia_page_extract():
    """test if data pulled from wikipedia can be written in a file"""
    global page_id_test
    fetcher = WikiFetcher()
    fetcher.fetch_wiki_extract(page_id_test)
    path = fetcher.to_file("test.txt")
    file = Path(path)
    assert file.is_file() is True

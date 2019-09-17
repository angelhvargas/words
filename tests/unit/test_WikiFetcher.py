from WikiFetcher import WikiFetcher


def test_can_fetch_wikipedia_page_extract_with_given_id():
    """test if class WikiFetcher can fetch/pull a page extract from Wikipedia"""
    page_id_test = 21721040
    fetcher = WikiFetcher()
    data = fetcher.fetch_wiki_extract(page_id_test)
    assert len(data["query"]["pages"][str(page_id_test)]["extract"]) > 0

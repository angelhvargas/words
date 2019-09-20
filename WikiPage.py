
class WikiPage:
    """WikiPage DTO"""
    ##################
    # attributes

    # page_id
    _page_id = None

    # page_title
    _title = None

    # page_extract
    _extract = None

    def __init__(self, **kwargs):
        self.page_id = kwargs.pop('page_id')
        self.title = kwargs.pop('title')
        self.extract = kwargs.pop('extract')

    # getters
    @property
    def title(self):
        return self._title

    @property
    def extract(self):
        return self._extract

    @property
    def page_id(self):
        return self._page_id

    @title.setter
    def title(self, title):
        self._title = title

    @extract.setter
    def extract(self, extract):
        self._extract = extract

    @page_id.setter
    def page_id(self, page_id):
        self._page_id = page_id

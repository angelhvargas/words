import requests
from pathlib import Path
from WikiPage import WikiPage


class WikiFetcher:
    """class WikiFetcher handle to fetch plain text
    or limited HTML extracts of the given page"""

    ##########################
    # attributes

    # WikiPage DTO
    wiki_page = None

    # api endpoint uri
    page_extract_api_url = "https://en.wikipedia.org/w/api.php"

    def fetch_wiki_extract(self, page_id):
        """fetch_wiki_extract fetch an extract from the wikipedia
        api and returns a json object with the response"""
        endpoint = self.page_extract_api_url

        session = requests.Session()

        params = {
            "action": "query",
            "prop": "extracts",
            "pageids": page_id,
            "explaintext": 1,
            "format": "json"
        }

        try:
            response = session.get(url=endpoint, params=params)
        except requests.exceptions.Timeout:
            return {
                "error": "request took too long"
            }
        except requests.exceptions.TooManyRedirects:
            return {
                "error": "too many redirects"
            }
        except requests.exceptions.RequestException as e:
            return {
                "error": e
            }

        data = {
            "title": response.json()["query"]["pages"][str(page_id)]["title"],
            "extract": response.json()["query"]["pages"][str(page_id)]["extract"]
        }

        self.wiki_page = WikiPage(page_id=page_id, title=data["title"], extract=data["extract"])

        return self.wiki_page

    def to_file(self, filename="output.txt"):
        """write extract to a file and returns the absolute path to it"""
        with open(filename, "w+", encoding='utf-8') as file:
            file.write(self.wiki_page.extract)
            file.close()

        absolute_path = Path(filename)
        return absolute_path

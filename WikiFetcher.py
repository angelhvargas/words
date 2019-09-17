import requests
from pathlib import Path


class WikiFetcher:
    """class WikiFetcher handle to fetch plain text
    or limited HTML extracts of the given page"""

    ##########################
    # attributes

    # api endpoint uri
    page_extract_api_url = "https://en.wikipedia.org/w/api.php"

    # page extract
    extract = ""

    # path to file
    absolute_path = ""

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

        self.extract = response.json()["query"]["pages"][str(page_id)]["extract"]
        return self.extract

    def to_file(self, filename="output.txt"):
        """write extract to a file and returns the absolute path to it"""
        with open(filename, "w+", encoding='utf-8') as file:
            file.write(self.extract)
            file.close()

        self.absolute_path = Path(filename)
        return self.absolute_path

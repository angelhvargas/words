import requests


class WikiFetcher:
    """class WikiFetcher handle to fetch plain text
    or limited HTML extracts of the given page"""

    ##########################
    # attributes

    # api endpoint uri
    page_extract_api_url = "https://en.wikipedia.org/w/api.php"

    def fetch_wiki_extract(self, id):
        """fetch_wiki_extract fetch an extract from the wikipedia
        api and returns a json object with the response"""
        endpoint = self.page_extract_api_url

        session = requests.Session()

        params = {
            "action": "query",
            "prop": "extracts",
            "pageids": id,
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

        data = response.json()
        return data

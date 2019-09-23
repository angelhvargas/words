import requests
from WikiPage import WikiPage


class WikiAPIClient:
    """class WikiAPIClient handle to fetch plain text
    or limited HTML extracts of the given page"""

    ##########################
    # attributes

    # WikiPage DTO
    wiki_page = None

    def get_wiki_page_extract(self, page_id: int):
        """
        get_wiki_page_extract

        Fetch an extract from the Wikipedia
        API and returns a WikiPage DTO object if the response is correct,
        otherwise will return a json

        :param page_id:
        :return:
        """

        api_endpoint = "https://en.wikipedia.org/w/api.php"

        params = {
            "action": "query",
            "prop": "extracts",
            "pageids": page_id,
            "explaintext": 1,
            "format": "json"
        }

        data = self.api_request(api_endpoint, params)

        if "error" in data:
            return False

        self.wiki_page = WikiPage(page_id=page_id, title=data["title"], extract=data["extract"])

        return self.wiki_page

    @staticmethod
    def api_request(api_endpoint: str, params: dict) -> dict:
        """
        api_request

        executes an api request to wikipedia API
        :param api_endpoint:
        :param params:
        :return:
        """

        # page_id
        page_id = str(params["pageids"])

        try:
            response = requests.get(url=api_endpoint, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()
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

        if response.status_code == 200 and "missing" not in data["query"]["pages"][page_id]:
            data = {
                "page_id": page_id,
                "title": data["query"]["pages"][page_id]["title"],
                "extract": data["query"]["pages"][page_id]["extract"]
            }

            return data
        else:
            return {
                "page_id": page_id,
                "error": "invalid page or doesn't exists"
            }


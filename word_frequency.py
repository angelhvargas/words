#!/usr/bin/env python3
"""
Word Frequency
--------------
Problem:

Write a program to fetch a Wikipedia page and report the top n words on that page.
The parameters to the program should be '_page_id' and 'n'.
The URL to fetch a page from Wikipedia is
https://en.wikipedia.org/w/api.php?action=query&prop=extracts&pageids=[PAGE
ID]&explaintext&format=json (replacing [PAGE ID] with the requested page id). This returns a
JSON object where the page's text is available under query.pages.[PAGE ID].extract and the title
under query.pages.[PAGE ID].title.
The output should look like this (where n = 5 and _page_id = 21721040):
URL:
https://en.wikipedia.org/w/api.php?action=query&prop=extracts&pageids=21721
040&explaintext&format=json
Title: Stack Overflow
Top 5 words:
- 21 stack, questions
- 16 overflow
- 11 that, users
- 10 site
- 7 answers, question
When two or more words have the same frequency, include them all on the same line separated
by a comma.
A word is defined as a sequence of at least four alphabetic characters.
Include unit tests and a README describing how to compile (if necessary) and run your solution.

Author: Angel Vargas
"""

import argparse

from WordsProcessor import WordsProcessor
from WikiAPIClient import WikiAPIClient
from WikiPage import WikiPage

NUMBER = None
_page_id = None


def process(_page_id: int, _number: int) -> None:
    """
    Main execution thread.
    :param _page_id: wikipedia page id
    :param _number: number of results.
    :return:
    """
    wiki_api_client = WikiAPIClient()
    word_processor = WordsProcessor()
    # gets dto
    wiki_page = wiki_api_client.get_wiki_page_extract(_page_id)
    # load data to file
    word_processor.load_data(wiki_page)
    # process map-reduce to count words
    words = word_processor.process()
    # sort words descending based on their repetition value
    sorted_words = dict(sorted(words.items(), key=lambda x: x[1], reverse=True))
    # invert and group the dictionary for easy printing and aggregates words with same number of repetitions.
    _reverse_dict = {}
    for k, v in sorted_words.items():
        try:
            if len(_reverse_dict) >= _number:
                break
            _reverse_dict[v] += ", "+k
        except Exception:
            _reverse_dict[v] = str(k)

    print_output(wiki_page, _reverse_dict)


def print_output(_wikipage: WikiPage, _sorted_results: dict) -> None:
    """
    print a nice output to the user
    :param _wikipage:
    :param _sorted_results:
    :return:
    """
    global NUMBER
    """
    
    :param _dictionary:
    :return: None
    """
    print("Title: " + str(_wikipage.title))
    print("Top " + str(NUMBER) + " words:")
    for value, word in _sorted_results.items():
        print("- " + str(value) + " " + word)


def _launch() -> None:
    """
    Process arguments and prepare program to run, also process user input
    :return: None
    """
    global NUMBER, _page_id

    # process user input
    parser = argparse.ArgumentParser(prog='python3 -m word_frequency',
                                     description=__doc__)
    parser.add_argument('-n', '--number', type=int)
    parser.add_argument('-p', '--page_id', type=int)

    args = parser.parse_args()
    _page_id = args.page_id
    NUMBER = args.number

    process(_page_id, NUMBER)


if __name__ == '__main__':
    """
        Starts program
    """
    _launch()

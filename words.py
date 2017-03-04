#! /usr/bin/env python3
# url = http://sixty-north.com/c/t.txt
import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words form a url

    Args:
        url: The url is http://sixty-north.com/c/t.txt

    Returns:
        a list of strings containing the words from the url
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    for word in items:
            print(word)


def main(url):
    words = fetch_words(url)
    print_items(words)

# making this function a script you need the bottom bit.
if __name__ == '__main__':
    main(sys.argv[1])

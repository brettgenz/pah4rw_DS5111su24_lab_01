import os, logging, sys

relative_path = os.path.abspath('./../')
sys.path.append(relative_path)

from data_prep import *

logging.basicConfig(level = logging.INFO, stream = sys.stderr,
                    format = '%(asctime)s %(name)s %(levelname)s: %(message)s'
                   )

log = logging.getLogger(__name__)


def test_tokenize_text():
    """
    Given a string _text_ of text with the combined content of all 4 English books, which have already been through the 
    clean_text() function (i.e., has been converted to lowercase and had punctuation removed) ...
    When I pass _text_ to the tokenize_text() function ...
    Then the output for each book should be a list of length 89023, indicating that tokenize_text() returned the 
    correct number of tokens.
    """
    
    combined_text = ""

    books = [
        "./../pg17192.txt",
        "./../932.txt",
        "./../1063.txt",
        "./../10031-0.txt",
        # "./../pg14082.txt"
        ]

    for book in books:
        with open(book, 'r') as file:
            combined_text += file.read()

    output = tokenize_text(clean_text(combined_text))
    
    try:
        assert len(output) == 89023, f"tokenize_text() returned an incorrect number of tokens for the combined set of books"
        log.info(f"Test passed: tokenize_text() returned the correct number of tokens")
    except AssertionError as e:
        log.info(f"Test failed: caught an assertion error with message: {e}")


if __name__ == '__main__':

    test_tokenize_text()
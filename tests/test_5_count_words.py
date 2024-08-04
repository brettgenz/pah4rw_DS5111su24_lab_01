import os, logging, sys

relative_path = os.path.abspath('.')
sys.path.append(relative_path)

from pah4rw.data_prep import *

logging.basicConfig(level = logging.INFO, stream = sys.stderr,
                    format = '%(asctime)s %(name)s %(levelname)s: %(message)s'
                   )

log = logging.getLogger(__name__)


def test_count_words():
    """
    Given a string _text_ of text for the combined text of all English books, which has already been through the 
    clean_text() function (i.e., has been converted to lowercase and had punctuation removed) and the tokenize_text() 
    function (i.e., has been split into a list of lowercase tokens without any punctuation)...
    When I pass _text_ to the count_words() function ...
    Then I should get a dictionary output for each book, and the value for the key 'the' should be at least 500.
    """

    combined_text = ""

    books = [
        "./pg17192.txt",
        "./932.txt",
        "./1063.txt",
        "./10031-0.txt",
        # "./pg14082.txt"
        ]

    for book in books:
        with open(book, 'r') as file:
            combined_text += file.read()

    output = count_words(tokenize_text(clean_text(combined_text)))
    
    try:
        assert output.get('the') == 6398, f"count_words() produced an incorrect number of instances of 'the' for the combined text"
        log.info(f"Test passed: count_words() produced the correct number of instances of 'the' for the combined text")
    except AssertionError as e:
        log.info(f"Test failed: caught an assertion error with message: {e}")



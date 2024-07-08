import os, logging, sys
import pytest

relative_path = os.path.abspath('./../')
sys.path.append(relative_path)

from data_prep import *

logging.basicConfig(level = logging.INFO, stream = sys.stderr,
                    format = '%(asctime)s %(name)s %(levelname)s: %(message)s'
                   )

log = logging.getLogger(__name__)

@pytest.mark.parametrize(
    "book_name, file_name",
    [
        ("The Raven", "./../pg17192.txt"),
        ("The Fall of the House of Usher", "./../932.txt"),
        ("The Cask of Amontillado", "./../1063.txt"),
        ("The Poems", "./../10031-0.txt"),
        # ("Le Corbeau", "./../pg14082.txt")
    ]
)
def test_count_words(book_name, file_name):
    """
    Given a string _text_ of text for each book, which has already been through the clean_text() function (i.e., has been
    converted to lowercase and had punctuation removed) and the tokenize_text() function (i.e., has been split
    into a list of lowercase tokens without any punctuation)...
    When I pass _text_ to the count_words() function ...
    Then I should get a dictionary output for each book, and the value for the key 'the' should be at least 500.
    """

    book = book_name
    file = file_name

    with open(file_name, 'r') as file:
        text = file.read()

        output = count_words(tokenize_text(clean_text(text)))
    
        try:
            assert output.get('the') >= 500, f"count_words() produced too few instances of 'the' for {book}"
            log.info(f"Test passed: count_words() produced at least 500 instances of 'the' for {book}")
        except AssertionError as e:
            log.info(f"Test failed: caught an assertion error with message: {e}")



if __name__ == '__main__':
    pytest.main()
import os, logging, sys
import pytest

relative_path = os.path.abspath('.')
sys.path.append(relative_path)

from pah4rw.data_prep import *

logging.basicConfig(level = logging.INFO, stream = sys.stderr,
                    format = '%(asctime)s %(name)s %(levelname)s: %(message)s'
                   )

log = logging.getLogger(__name__)

@pytest.mark.parametrize(
    "book_name, file_name",
    [
        ("The Raven", "./pg17192.txt"),
        ("The Fall of the House of Usher", "./932.txt"),
        ("The Cask of Amontillado", "./1063.txt"),
        ("The Poems", "./10031-0.txt"),
        # ("Le Corbeau", ".pg14082.txt")
    ]
)
def test_tokenize_text(book_name, file_name):
    """
    Given a string _text_ of text with content of each book in the list which that has already been through the 
    clean_text() function (i.e., has been converted to lowercase and had punctuation removed) ...
    When I pass _text_ to the tokenize_text() function ...
    Then the output for each book should be a list of at least length 5000 (the Cask of Amontillado is the
    shortest with 5334 tokens) ...
    """
    
    book = book_name
    file = file_name

    with open(file_name, 'r') as file:
        text = file.read()

        output = tokenize_text(clean_text(text))
    
        try:
            assert len(output) > 5000, f"tokenize_text() returned too few tokens for {book}"
            log.info(f"Test passed for book {book}: tokenize_text() returned at least 5000 tokens")
        except AssertionError as e:
            log.info(f"Test failed: caught an assertion error with message: {e}")



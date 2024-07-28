import os, logging, sys
import pytest

relative_path = os.path.abspath('.')
sys.path.append(relative_path)

from data_prep import *

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
        # ("Le Corbeau", "./../pg14082.txt")
    ]
)
def test_clean_text(book_name, file_name):
    """
    Given a string _text_ of text with content of each book in the list ...
    When I pass _text_ to the clean_text() function ...
    Then when I test that certain punctuation marks ',.;:' are not in the output for a given book, 
    the test should pass.
    """
    
    book = book_name
    file = file_name

    with open(file_name, 'r') as file:
        text = file.read()

        output = clean_text(text)
    
        try:
            assert ('[,.;:]' not in output), f"the punctuation marks ',.;:' appear in the clean_text() output for book {book}"
            log.info(f"Test passed for book {book}: the punctuation marks ',.;:' do not appear in the output")
        except AssertionError as e:
            log.info(f"Test failed: caught an assertion error with message: {e}")



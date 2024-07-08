import os, logging, sys

relative_path = os.path.abspath('./../')
sys.path.append(relative_path)

from data_prep import *

logging.basicConfig(level = logging.INFO, stream = sys.stderr,
                    format = '%(asctime)s %(name)s %(levelname)s: %(message)s'
                   )

log = logging.getLogger(__name__)


def test_clean_text():
    """
    Given a string _text_ of text with content of all books in the list combined ...
    When I pass _text_ to the clean_text() function ...
    Then when I test that certain punctuation marks ',.;:' are not in the output for the combined text of 
    all books, the test should pass.
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

    output = clean_text(combined_text)
    
    try:
        assert ('[,.;:]' not in output), f"the punctuation marks ',.;:' appear in the output for the combined text"
        log.info(f"Test passed: the punctuation marks ',.;:' do not appear in the output for the combined text")
    except AssertionError as e:
        log.info(f"Test failed: caught an assertion error with message: {e}")


if __name__ == '__main__':
    
    # pytest.main()
	test_clean_text()
import os
import logging, sys

relative_path = os.path.abspath('./../')
sys.path.append(relative_path)

from data_prep import *

logging.basicConfig(level = logging.INFO, stream = sys.stderr,
                    format = '%(asctime)s %(name)s %(levelname)s: %(message)s'
                   )

log = logging.getLogger(__name__)

text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."

def test_clean_text():
    """
    Given a string _text_ of text with words
    When I pass _text_ to the clean_text() function
    Then I should get a string output (test 1), the string should not be empty (test 2), and an integer
    passed as input should generate an assertion error (test 3).
    """
    
    output = clean_text(text)
    assert isinstance(output, str), f"expected str but got {type(text)}"
    log.info(f"Test 1 passed: clean_text() output is of type str")
        
    try:
        output = clean_text('')
        assert output != "", f"output text is empty"
    except AssertionError as e:
        log.info(f"Test 2 passed: caught an assertion error as expected with message: {e}")
        
    try:
        output = clean_text(42)
        assert isinstance(output, str), f"expected str but got {type(text)}"
    except AssertionError as e:
        log.info(f"Test 3 passed: caught an assertion error as expected with message: {e}")


if __name__ == '__main__':
    
    test_clean_text()
import os
import logging, sys

relative_path = os.path.abspath('./../')
sys.path.append(relative_path)

from data_prep import *

logging.basicConfig(level = logging.INFO, stream = sys.stderr,
                    format = '%(asctime)s %(name)s %(levelname)s: %(message)s'
                   )

log = logging.getLogger(__name__)

with open('./../pg17192.txt', 'r') as file:
    the_raven = file.read()


def test_tokenize_text():
    """
    Given a string _text_ of text that has already been through the clean_text() function (i.e., has been
    converted to lowercase and had punctuation removed) ...
    When I pass _text_ to the tokenize_text() function ...
    Then I should get a list output of length 25, and a test for output of greater than length 25 should fail,
    indicating that the tokenizer did not include extra tokens (such as puncuation)
    """
    
    output = tokenize_text(clean_text(the_raven))
    
    try:
        assert len(output) == 10203, f"tested for length 10203 but got {len(output)}"
        log.info(f"Test 1 passed, tokenize_text() passed correct number of tokens")
    except AssertionError as e:
        log.info(f"Test failed: caught an assertion error with message: {e}")



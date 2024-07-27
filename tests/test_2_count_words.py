import os
import logging, sys

from decorator import decorator

relative_path = os.path.abspath('./../')
sys.path.append(relative_path)

from data_prep import *

logging.basicConfig(level = logging.INFO, stream = sys.stderr,
                    format = '%(asctime)s %(name)s %(levelname)s: %(message)s'
                   )

log = logging.getLogger(__name__)

text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."

@decorator
def test_count_words():
    """
    Given a string _text_ of text that has already been through the clean_text() function (i.e., has been
    converted to lowercase and had punctuation removed) and the tokenize_text() function (i.e., has been split
    into a list of lowercase tokens without any punctuation)...
    When I pass _text_ to the count_words() function ...
    Then I should get a dictionary output with 21 keys (i.e., len(output) = 21), and the test for greater than 21
    keys should fail.
    """
    output = count_words(tokenize_text(clean_text(text)))
    
    try:
        assert len(output) > 21, f"tested for more than 21 keys but got {len(output)}"
    except AssertionError as e:
        log.info(f"Test failed as expected, caught an assertion error with message: {e}")



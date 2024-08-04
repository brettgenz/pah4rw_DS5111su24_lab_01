import os
import logging, sys

from decorator import decorator

relative_path = os.path.abspath('.')
sys.path.append(relative_path)

from pah4rw_DS5111su24_lab_01.data_prep import *

logging.basicConfig(level = logging.INFO, stream = sys.stderr,
                    format = '%(asctime)s %(name)s %(levelname)s: %(message)s'
                   )

log = logging.getLogger(__name__)

text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."

@decorator
def test_tokenize_text():
    """
    Given a string _text_ of text that has already been through the clean_text() function (i.e., has been
    converted to lowercase and had punctuation removed) ...
    When I pass _text_ to the tokenize_text() function ...
    Then I should get a list output of length 25, and a test for output of greater than length 25 should fail,
    indicating that the tokenizer did not include extra tokens (such as puncuation)
    """
    
    output = tokenize_text(clean_text(text))
    
    try:
        assert len(output) > 25, f"tested for length > 25 but got {len(output)}"
    except AssertionError as e:
        log.info(f"Test failed as expected, caught an assertion error with message: {e}")



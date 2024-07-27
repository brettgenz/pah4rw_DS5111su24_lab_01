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

def test_tokenize_text():
    """
    Given a string _text_ of text that has already been through the clean_text() function (i.e., has been
    converted to lowercase and had punctuation removed) ...
    When I pass _text_ to the tokenize_text() function ...
    Then I should get a list output (test 1), and the list should be of length 25 (test 2)
    """
    
    output = tokenize_text(text)
    assert isinstance(output, list), f"expected output to be a list but got {type(output)}"
    log.info(f"Test 1 passed: tokenize_text() output is of type list")

    assert len(tokenize_text(clean_text(text))) == 25, f"expected list of length 25 but got {len(tokenize_text(clean_text(text)))}"
    log.info(f"Test 2 passed: tokenize_text() returned the correct number of tokens")



import os
import logging, sys

relative_path = os.path.abspath('.')
sys.path.append(relative_path)

from data_prep import *

logging.basicConfig(level = logging.INFO, stream = sys.stderr,
                    format = '%(asctime)s %(name)s %(levelname)s: %(message)s'
                   )

log = logging.getLogger(__name__)

text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."

def test_count_words():
    """
    Given a string _text_ of text that has already been through the clean_text() function (i.e., has been
    converted to lowercase and had punctuation removed) and the tokenize_text() function (i.e., has been split
    into a list of lowercase tokens without any punctuation)...
    When I pass _text_ to the count_words() function ...
    Then I should get a dictionary output (test 1), and the key for the word 'raven' in that dictionary should
     have a value of 1 (test 2).
    """
    output = count_words(tokenize_text(clean_text(text)))
    assert isinstance(output, dict), f"expected output to be a dict but got {type(output)}."
    log.info(f"Test 1 passed: count_words() output is of type dict")

    assert output.get('raven') == 1, f"expected count of 1 but got {output.get('raven')}."
    log.info(f"Test 2 passed: count_words() counted the correct number of occurrences of the word 'raven'.")


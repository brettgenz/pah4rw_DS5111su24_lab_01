import os
import logging, sys

from decorator import decorator

relative_path = os.path.abspath('.')
sys.path.append(relative_path)

from pah4rw.data_prep import *

logging.basicConfig(level = logging.INFO, stream = sys.stderr,
                    format = '%(asctime)s %(name)s %(levelname)s: %(message)s'
                   )

log = logging.getLogger(__name__)

text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."


@decorator
def test_clean_text():
    """
    Given a string _text_ of text with words
    When I pass _text_ to the clean_text() function
    Then when I search for the word 'Raven' with a capital R in the output, the test should fail (test 1).
    """
    
    output = clean_text(text)
    
    # log.info(f"Test 1 failed as intended: no instance of Raven with a capital R appears in the output")

    try:
        output = clean_text(text)
        assert ('Raven' in output), "the word 'Raven' does not appear in the output"
    except AssertionError as e:
        log.info(f"Test 1 failed as expected, caught an assertion error as expected with message: {e}")



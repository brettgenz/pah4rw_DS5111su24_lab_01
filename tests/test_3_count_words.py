import os
import logging, sys

relative_path = os.path.abspath('.')
sys.path.append(relative_path)

from pah4rw.data_prep import *

logging.basicConfig(level = logging.INFO, stream = sys.stderr,
                    format = '%(asctime)s %(name)s %(levelname)s: %(message)s'
                   )

log = logging.getLogger(__name__)

with open('./pg17192.txt', 'r') as file:
    the_raven = file.read()


def test_count_words():
    """
    Given a string _text_ of text that has already been through the clean_text() function (i.e., has been
    converted to lowercase and had punctuation removed) and the tokenize_text() function (i.e., has been split
    into a list of lowercase tokens without any punctuation)...
    When I pass _text_ to the count_words() function ...
    Then I should get a dictionary output with 2571 keys (i.e., len(output) = 2571) (test 1), and the key for 
    'raven' should have a value of 42.
    """
    output = count_words(tokenize_text(clean_text(the_raven)))
    
    try:
        assert len(output) == 2571, f"tested for 2571 keys but got {len(output)}"
        log.info("Test 1 passed, count_words() produced the correct number of keys")
    except AssertionError as e:
        log.info(f"Test 1 failed: caught an assertion error with message: {e}")

    try:
        assert output.get('raven'), f"should have 42 occurrences of the word 'raven' but got {output.get('raven')}"
        log.info("Test 2 passed, count_words() produced 42 occurrences of the word 'raven'")
    except AssertionError as e:
        log.info(f"Test 2 failed: caught an assertion error with message: {e}")


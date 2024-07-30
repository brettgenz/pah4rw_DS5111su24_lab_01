import os
import logging, sys
import requests

relative_path = os.path.abspath('.')
sys.path.append(relative_path)

from data_prep import *

logging.basicConfig(level = logging.INFO, stream = sys.stderr,
                    format = '%(asctime)s %(name)s %(levelname)s: %(message)s'
                   )

log = logging.getLogger(__name__)

url = 'https://www.gutenberg.org/cache/epub/17192/pg17192.txt'
response = requests.get(url)
the_raven = response.text
# try:
#     with open('./pg17192.txt', 'r') as file:
#         the_raven = file.read()
# except:
#     response = requests.get(url)
#     the_raven = response.text


def test_clean_text():
    """
    Given a string _text_ of text with content of the book 'The Raven' ...
    When I pass _text_ to the clean_text() function ...
    Then when I test that the word 'Raven' with a capital R is not in the output, the test should pass (test 1), and
    when I test that certain punctuation marks ',.;:' are not in the output, the test should pass (test 2).
    """
    
    output = clean_text(the_raven)
    
    # log.info(f"Test 1 failed as intended: no instance of Raven with a capital R appears in the output")

    try:
        assert ('Raven' not in output), "the word 'Raven' appears in the output"
        log.info("Test 1 passed: the word 'Raven' was not in the output.")
    except AssertionError as e:
        log.info(f"Test 1 failed: caught an assertion error with message: {e}")
    
    try:
        assert ('[,.;:]' not in output), "the punctutation marks ',.;:' do appear in the output"
        log.info("Test 2 passed: the punctutation marks ',.;:' do not appear in the output")
    except AssertionError as e:
        log.info(f"Test 2 failed: caught an assertion error with message: {e}")
    


if __name__ == '__main__':
    test_clean_text()

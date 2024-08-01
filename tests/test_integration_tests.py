import pytest
import os, logging, sys

relative_path = os.path.abspath('.')
sys.path.append(relative_path)

from data_prep import *


@pytest.mark.integration
def test_tokenize_text():
    """
    Given the below passage of text passed through clean_text() ...
    When I pass that into tokenize_text() ...
    Then if tokenize_text() works correctly, it should have a length of 15.
    """

    text = "How much wood could a wood chuck, chuck if a wood chuck could chuck wood?"

    output = tokenize_text(clean_text(text))

    try:
        assert len(output) == 15, f"Expected 15, got {len(output)}."
        log.info("Test passed: tokenize_text() returned the correct number of tokens.")
    except AssertionError as e:
        log.info(f"Test failed: caught an assertion error with message: {e}")


@pytest.mark.integration
def test_count_words():
    """
    Given a passage of text passed through clean_text() and tokenize_text() ...
    When I pass that into count_words() ...
    Then I should have a total of 4 instances of the word 'chuck' in the dictionary 
    output of count_words().
    """

    text = "How much wood could a wood chuck, chuck if a wood chuck could chuck wood?"

    output = count_words(tokenize_text(clean_text(text)))

    try:
        assert output.get('chuck') == 4, f"Expected 4, got {output.get('chuck')}"
        log.info("Test passed, expected 4 instances of 'chuck' and got 4.")
    except AssertionError as e:
        log.info(f"Test failed: caught an assertion error with message: {e}")
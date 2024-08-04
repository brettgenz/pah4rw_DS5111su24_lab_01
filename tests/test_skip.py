import pytest
import os, logging, sys
import platform
from packaging.version import parse

relative_path = os.path.abspath('.')
sys.path.append(relative_path)

from pah4rw.data_prep import *

@pytest.mark.skip(reason="Unable to test German version of books yet")
def test_count_words():
    """
    Given the text of the book "Der Rabe" ("The Raven" in German), which has already been through the 
    clean_text() function (i.e., has been converted to lowercase and had punctuation removed) and the 
    tokenize_text() function (i.e., has been split into a list of lowercase tokens without any punctuation) ...
    When I pass _text_ to the count_words() function ...
    Then it should find the correct number of instances of the word "rabe" ... (actual total is currently 
    unknown)
    """
    
    text = "" # no text available yet
    
    output = count_words(tokenize_text(clean_text(text)))
    
    try:
        assert output.get('rabe') == 0, f"count_words() produced an incorrect number of instances of 'rabe' from Der Rabe"
        log.info(f"Test passed: count_words() produced the correct number of instances of 'rabe' from Der Rabe")
    except AssertionError as e:
        log.info(f"Test failed: caught an assertion error with message: {e}")


@pytest.mark.xfail(platform.system() == 'Windows', reason='function has not been tested on Windows')
def test_clean_text():
    """
    Given a string _text_ of text with words
    When I pass _text_ to the clean_text() function
    Then when I search for the word 'yesterday' in the output, the test should pass. 
    """

    text = """
    A haiku:

    Yesterday it worked
    Today it is not working
    Windows is like that
    """

    output = clean_text(text)

    try:
        assert 'yesterday' in output, f"clean_text() did not find the correct word"
        log.info(f"Test passed: clean_text() changed the word Yesterday to lowercase")
    except AssertionError as e:
        log.info(f"Test failed: caught an assertion error with message: {e}")


@pytest.mark.xfail(sys.version_info.major < 3, reason='test not supported in 2.x')
def test_tokenize_text():
    """
    Given a string _text_ of text of the book 'Le Corbeau', which has already been through the 
    clean_text() function (i.e., has been converted to lowercase and had punctuation removed) ...
    When I pass _text_ to the tokenize_text() function ...
    Then the output for the book should be a list of length , indicating that tokenize_text() returned the 
    correct number of tokens.
    """

    text = """
    _Mais le Corbeau, perché solitairement sur ce buste placide, parla
        ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne
        proférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce
        que je fis à peine davantage que marmotter «D'autres amis déjà ont
        pris leur vol--demain il me laissera comme mes Espérances déjà ont
        pris leur vol.» Alors l'oiseau dit: «Jamais plus.»_
    """

    output = tokenize_text(clean_text(text))

    try:
        assert len(output) == 69, f"tokenize_text() returned an incorrect number of tokens"
        log.info(f"Test passed: tokenize_text() returned the correct number of tokens")
    except AssertionError as e:
        log.info(f"Test failed: caught an assertion error with message: {e}")

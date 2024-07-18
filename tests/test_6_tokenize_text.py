import os, logging, sys

relative_path = os.path.abspath('./../')
sys.path.append(relative_path)

from data_prep import *

logging.basicConfig(level = logging.INFO, stream = sys.stderr,
                    format = '%(asctime)s %(name)s %(levelname)s: %(message)s'
                   )

log = logging.getLogger(__name__)

text = """
_Mais le Corbeau, perché solitairement sur ce buste placide, parla
    ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne
    proférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce
    que je fis à peine davantage que marmotter «D'autres amis déjà ont
    pris leur vol--demain il me laissera comme mes Espérances déjà ont
    pris leur vol.» Alors l'oiseau dit: «Jamais plus.»_
"""


def test_tokenize_text():
    """
    Given a string _text_ of text of the book 'Le Corbeau', which has already been through the 
    clean_text() function (i.e., has been converted to lowercase and had punctuation removed) ...
    When I pass _text_ to the tokenize_text() function ...
    Then the output for the book should be a list of length , indicating that tokenize_text() returned the 
    correct number of tokens.
    """

    output = tokenize_text(clean_text(text))
    
    try:
        assert len(output) == 69, f"tokenize_text() returned an incorrect number of tokens for the combined set of books"
        log.info(f"Test passed: tokenize_text() returned the correct number of tokens")
    except AssertionError as e:
        log.info(f"Test failed: caught an assertion error with message: {e}")


if __name__ == '__main__':

    test_tokenize_text()
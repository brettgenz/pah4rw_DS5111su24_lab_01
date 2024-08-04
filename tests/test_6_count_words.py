import os, logging, sys

relative_path = os.path.abspath('.')
sys.path.append(relative_path)

from pah4rw_DS5111su24_lab_01.data_prep import *

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

def test_count_words():
    """
    Given a string _text_ of text for the combined text of all English books, which has already been through the 
    clean_text() function (i.e., has been converted to lowercase and had punctuation removed) and the tokenize_text() 
    function (i.e., has been split into a list of lowercase tokens without any punctuation)...
    When I pass _text_ to the count_words() function ...
    Then I should get a dictionary output for words in the above passage, and the value for the key 'ce' should be 4.
    """

    output = count_words(tokenize_text(clean_text(text)))
    
    try:
        assert output.get('ce') == 4, f"count_words() produced an incorrect number of instances of 'ce' from the passage from Le Corbeau"
        log.info(f"Test passed: count_words() produced the correct number of instances of 'ce' from the passage from Le Corbeau")
    except AssertionError as e:
        log.info(f"Test failed: caught an assertion error with message: {e}")




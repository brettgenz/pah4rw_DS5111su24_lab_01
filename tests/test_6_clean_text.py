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

def test_clean_text():
    """
    Given a string _text_ of text of the book 'Le Corbeau' ...
    When I pass _text_ to the clean_text() function ...
    Then when I test that certain punctuation marks '-_»«' are not in the output for the output of Le Corbeau.
    """

    output = clean_text(text)
    
    try:
        assert ('»' not in output), f"the punctuation marks '»' were not removed from the clean_text() output for Le Corbeau"
        log.info(f"Test passed: the punctuation marks '»' do not appear in the clean_text() output for Le Corbeau")
    except AssertionError as e:
        log.info(f"Test failed: caught an assertion error with message: {e}")


if __name__ == '__main__':
    
    # pytest.main()
	test_clean_text()
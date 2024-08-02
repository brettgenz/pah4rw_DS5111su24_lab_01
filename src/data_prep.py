import string
import logging
import sys

logging.basicConfig(level = logging.INFO, stream = sys.stderr,
                    format = '%(asctime)s %(name)s %(levelname)s: %(message)s'
                   )

log = logging.getLogger(__name__)

def clean_text(input_text):
    """
    Input: a string
    Output: the input string with punctuation removed and letters converted to lowercase
    """
    assert isinstance(input_text, str), f"expected str but got {type(input_text)}"

    trans = str.maketrans('', '', string.punctuation)

    output_text = input_text.lower().translate(trans)
    assert isinstance(output_text, str), f"expected str but got {type(output_text)}"
    assert output_text != "", "output text is empty"

    return output_text


def tokenize_text(input_text):
    """
    Input: a string
    Output: a list of strings
    """
    assert isinstance(input_text, str), f"expected str but got {type(input_text)}"

    return str.split(input_text)


def count_words(input_list):
    """
    Input: a list of strings (tokens)
    Output: a dictionary of a frequency table of words (tokens) from the input list
    """
    assert isinstance(input_list, list), f"expected list but got {type(input_list)}"

    word_counts = {}

    for word in input_list:
        word_counts[word] = word_counts.get(word, 0) + 1

    assert isinstance(word_counts, dict)

    return word_counts

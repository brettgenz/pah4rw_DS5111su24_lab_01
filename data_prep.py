import string
import logging, sys

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
    
    assert type(word_counts) == dict
    
    return word_counts


sample_text_1 = "I could really use a nice, cold Vienna Lager from Devil's Backbone Brewery."
sample_text_2 = "How much wood could a wood chuck chuck if a wood chuck could chuck wood?"


def test_clean_text():
    output = clean_text(sample_text_1)
    assert isinstance(output, str), f"expected str but got {type(input_text)}"
    log.info(f"Test 1 passed: clean_text() output is of type str")
        
    try:
        output = clean_text('')
        assert output != "", f"output text is empty"
    except AssertionError as e:
        log.info(f"Test 2 passed: caught an assertion error as expected with message: {e}")
        
    try:
        output = clean_text(42)
        assert isinstance(output, str), f"expected str but got {type(input_text)}"
    except AssertionError as e:
        log.info(f"Test 3 passed: caught an assertion error as expected with message: {e}")
    
def test_tokenize_text():
    output = tokenize_text(sample_text_1)
    assert isinstance(output, list), f"expected output to be a list but got {type(output)}"
    log.info(f"Test 1 passed: tokenize_text() output is of type list")
    
    
def test_count_words():
    output = count_words(tokenize_text(clean_text(sample_text_2)))
    assert isinstance(output, dict)
    log.info(f"Test 1 passed: count_words() output is of type dict")

        
if __name__ == '__main__':
    
    test_clean_text()
    test_tokenize_text()
    test_count_words()
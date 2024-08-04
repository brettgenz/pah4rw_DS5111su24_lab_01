import os, logging, sys
import subprocess

relative_path = os.path.abspath('.')
sys.path.append(relative_path)

from pah4rw_DS5111su24_lab_01.data_prep import *

logging.basicConfig(level = logging.INFO, stream = sys.stderr,
                    format = '%(asctime)s %(name)s %(levelname)s: %(message)s'
                   )

log = logging.getLogger(__name__)

with open('./pg17192.txt', 'r') as file:
    text = file.read()

# keyword = 'raven'


def run_bash_command(command):
    """
    Takes a string containing the bash command as input, returns the output of the bash command.
    """

    result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout.strip()


def test_bash_vs_python_functions():
    """
    Given a text input of the book 'The Raven' ...
    When I run the text through the clean_text(), tokenize_text(), and count_words() functions, and compare
    that to the output of running 'cat {text} | grep -i raven | wc -l' ...
    Then I should get 46 instances of the word 'raven' for both methods.
    """

    filename = './pg17192.txt'

    bash_command = f"cat {filename} | grep -i raven | wc -l"
    bash_output = run_bash_command(bash_command)

    python_output = count_words(tokenize_text(clean_text(text)))

    # return print(python_output.get('raven'))
    try:
        assert int(bash_output) == python_output.get('raven'), f"Word counts do not match"
        log.info(f"Test passed: Python test and bash functions had the same output")
    except AssertionError as e:
        log.info(f"Test failed: caught an assertion error with message: {e}")


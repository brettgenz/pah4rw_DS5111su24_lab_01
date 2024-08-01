import os
import logging, sys

logging.basicConfig(level = logging.INFO, stream = sys.stderr,
                    format = '%(asctime)s %(name)s %(levelname)s: %(message)s'
                   )

log = logging.getLogger(__name__)

# need to create a guard so that I know what version is being run
# need to have an OR statement ... version 3.8 or 3.10

def test_version():
    """
    This test will pass if Python version 3.8 or 3.10 is used, but fail if a different 
    version is used.
    """

    try:
        assert (sys.version_info == 3.8 or sys.version_info == 3.10), "Python version not supported"
        log.info(f"Test passed: Current version of Python is supported")
    except AssertionError as e:
        log.info(f"Test failed: caught an assertion error with message: {e}")
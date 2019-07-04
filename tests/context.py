"""
    tests/context.py

    This file exists to provide a path context for automated tests, so that the
    user does not need to install the Python module in order to run the test
    suite.
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import web_mage

"""
    In all automated tests, you can now import the module context with the
    following:

    from .context import web_mage
"""

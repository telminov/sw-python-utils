# coding: utf-8
import os
import sys

test_dir = os.path.dirname(__file__)
sys.path.insert(0, test_dir)

import unittest
import swutils.tests

def runtests():
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner(verbosity=1)
    tests_dir = os.path.dirname(swutils.tests.__file__)
    suite_class = loader.discover(tests_dir)
    result = runner.run(suite_class)
    sys.exit(bool(result.failures))

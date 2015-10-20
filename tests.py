#! /usr/bin/env python
import unittest
import sys
from xmlrunner import XMLTestRunner
from colour_runner.runner import ColourTextTestRunner
from os import path


def thisDir():
    return path.dirname(path.realpath(__file__))

loader = unittest.TestLoader()
tests = loader.discover('.', pattern="test_*.py")

runner = ColourTextTestRunner()

if '--xml' in sys.argv:
    runner = XMLTestRunner(output='test-reports')

test_result = runner.run(tests)

if test_result.wasSuccessful():
    sys.exit()
else:
    number_failed = len(test_result.failures) + len(test_result.errors)
    sys.exit(number_failed)

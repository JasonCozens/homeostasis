#!/usr/bin/python3.1

import unittest

import tests.SimBaseTests
import tests.SimulatorTests

def alltests():
    return unittest.TestSuite([
        tests.SimBaseTests.alltests(),
        tests.SimulatorTests.alltests(),
        ])

def runalltests():
    unittest.TextTestRunner(verbosity=2).run(alltests())

if __name__ == "__main__":
    runalltests()

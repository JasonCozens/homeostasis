import unittest
import sys
import os	

sys.path.append(os.path.realpath(".."))

from cos import (
    SimBase,
    )

class SimBaseTests(unittest.TestCase):

    def test_InitSetsBuffers(self):
        outBuffers = []
        inBuffers = []
        simBase = SimBase(outBuffers, inBuffers)
        self.assertIs(simBase.OutBuffers, outBuffers)
        self.assertIs(simBase.InBuffers, inBuffers)

    def test_tick(self):
        simBase = SimBase([], [])
        self.assertRaises(NotImplementedError, simBase.tick)

def alltests():	
    return unittest.TestSuite([
        unittest.TestLoader().loadTestsFromTestCase(SimBaseTests),
        ])

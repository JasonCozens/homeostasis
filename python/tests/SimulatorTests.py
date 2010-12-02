import unittest
import sys
import os	

sys.path.append(os.path.realpath(".."))

from cos import (
    Simulator,
    )

class SimulatorTests(unittest.TestCase):

    def setUp(self):
        self.sim = Simulator()

    def test_SimulatorInit(self):
        self.assertEqual(self.sim.Count, 0)

    def test_IncIncreasesCount(self):
        self.sim.Inc()
        self.assertEqual(self.sim.Count, 1)

def alltests():	
    return unittest.TestSuite([
        unittest.TestLoader().loadTestsFromTestCase(SimulatorTests),
        ])



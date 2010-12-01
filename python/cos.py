import unittest

class Simulator:

    def __init__(self):
        self.Count = 0

    def Inc(self):
        self.Count = self.Count + 1

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

unittest.TextTestRunner(verbosity=2).run(alltests())

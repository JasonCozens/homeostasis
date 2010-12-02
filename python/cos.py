import unittest

class SimBase:

    def __init__(self, outBuffers, inBuffers):
        self.OutBuffers = outBuffers
        self.InBuffers = inBuffers

    def tick(self):
        return

class Simulator:

    def __init__(self):
        self.Count = 0

    def Inc(self):
        self.Count = self.Count + 1

class SimBaseTests(unittest.TestCase):

    def test_InitSetsBuffers(self):
        outBuffers = []
        inBuffers = []
        simBase = SimBase(outBuffers, inBuffers)
        self.assertIs(simBase.OutBuffers, outBuffers)
        self.assertIs(simBase.InBuffers, inBuffers)

    def test_tick(self):
        """Check that method is on SimBase."""
        simBase = SimBase([], [])
        simBase.tick()

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
        unittest.TestLoader().loadTestsFromTestCase(SimBaseTests),
        unittest.TestLoader().loadTestsFromTestCase(SimulatorTests),
        ])

unittest.TextTestRunner(verbosity=2).run(alltests())

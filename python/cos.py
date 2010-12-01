import unittest

class Simulator:

    def __init__(self):
        self.Step = 0

class SimulatorTests(unittest.TestCase):

    def test_SimulatorInit(self):
        sim = Simulator()
        self.assertEqual(sim.Step, 0)

def alltests():	
    return unittest.TestSuite([
        unittest.TestLoader().loadTestsFromTestCase(SimulatorTests),
        ])

unittest.TextTestRunner(verbosity=2).run(alltests())

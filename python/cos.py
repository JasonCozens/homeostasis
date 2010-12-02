

class SimBase:

    def __init__(self, outBuffers, inBuffers):
        self.OutBuffers = outBuffers
        self.InBuffers = inBuffers

    def tick(self):
        raise NotImplementedError()


class Simulator:

    def __init__(self):
        self.Count = 0

    def Inc(self):
        self.Count = self.Count + 1



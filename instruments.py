from time import sleep

class Result:
    def __init__(self, readouts):
        self.result = readouts

class AcmeInstruments:
    def initialize(self):
        # There's a very slow intialization here
        sleep(10)

    def run(self, pulses):
        # Run this in Acme QPU
        #...
        return Result([0.5, 0.0, 0.0, 0.5])  # Invent


class IBMInstruments:
    def run(self, pulses):
        # Run this in IBM QPU
        #...
        return Result([0.4, 0.1, 0.1, 0.4])  # Invent


class ZIInstruments:
    def run(self, pulses):
        # Run this in ZI QPU
        #...
        return Result([[0.25, 0.25, 0.25, 0.25]])  # Invent
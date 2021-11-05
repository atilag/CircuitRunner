from instruments import AcmeInstruments, IBMInstruments, ZIInstruments
from pulses import Pulse


class TaskRunner:
    def _compile(self, circuit, vendor):
        """ From circuit to vendor-specific pulse compilation """
        pulses = self._from_circuit_to_pulses(circuit, vendor)
        return pulses

    def _run_pulses(self, pulses, vendor):
        instrument = IBMInstruments()
        if vendor == "Acme":
            instrument = AcmeInstruments()
        if vendor == "IBM":
            instrument = IBMInstruments()
        if vendor == "ZI":
            instrument = ZIInstruments()

        instrument.initialize()
        return instrument.run(pulses)

    def _from_circuit_to_pulses(self, circuit, vendor):
        # Let's assume this transforms circuits to scheduled pulses
        pulses = []
        for gate in circuit.gates:
          pulse = gate.get("gate")()
          pulses.append(pulse.to_pulse(vendor))    
        return pulses    

  
    def run(self, circuit, vendor):
        p = self._compile(circuit, vendor)
        return self._run_pulses(p, vendor)
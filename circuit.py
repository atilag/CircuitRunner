from gates import *

class Circuit:
    def __init__(self):
        self.gates = []

    def add_gate(self, gate, qubits=None, clbits=None):

        self.gates.append(
            {
                "gate": gate,
                "params": None if not hasattr(gate, "params") else gate.params(),
                "qubits": qubits,
                "clbits": clbits,
            }
        )

    def get_gates(self):
        return self.gates

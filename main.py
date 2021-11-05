
# Requisites:
# - Has to support future new vendors (maybe hundreds)
# - Vendors will have their own compilation and instrument systems
# -
from gates import Measurement
from taskrunner import TaskRunner
from circuit import Circuit, CXGate, IDGate, XGate

if __name__ == '__main__':


  #  [q0] ---[X]---*----[Id]---[Meas]----------
  #                |             |
  #  [q1] --------[X]---[id]----------[Meas]---
  #                              |      |
  #  [c0] -----------------------*-------------
  #                                     |
  #  [c1] ------------------------------*------

  circuit = Circuit()
  circuit.add_gate(XGate, 0)
  circuit.add_gate(CXGate, [0, 1])
  circuit.add_gate(IDGate, [0, 1])
  circuit.add_gate(Measurement, [0, 1], [0, 1])
  task_runner = TaskRunner()
  result = task_runner.run(circuit, vendor="Acme")
  print(f"Statevector: {result.result}")

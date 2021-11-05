import numpy as np
from pulses import Pulse

class U3Gate:
    """ Parametrized gate """
    def __init__(self):
        self.theta = None
        self.phi = None
        self.lam = None

    def __str__(self):
        return "u3( " + self.theta + "," + self.phi + "," + self.lam + ")"


    def set_params(self, theta, phi, lam):
        self.theta = theta
        self.phi = phi
        self.lam = lam


    def get_params(self):
        return self.theta, self.phi, self.lam

  
    def to_pulse(self, vendor):
        if vendor == "Acme": 
            return Pulse.from_gate_parmas([self.theta, self.phi, self.lam])
        if vendor == "IBM":
            return Pulse.from_gate_parmas([self.theta, np.sqrt(self.phi), self.lam])
        if vendor == "ZI":
            return Pulse.from_gate_parmas([np.sqrt(self.theta)/2., self.phi, self.lam])

class XGate(U3Gate):
  def to_pulse(self, vendor):
    if vendor == "Acme": 
      return Pulse.from_gate_parmas([self.theta, self.phi, self.lam])
    if vendor == "IBM":
      return Pulse.from_gate_parmas([self.theta, self.phi, self.lam])
    if vendor == "ZI":
      return Pulse.from_gate_parmas([self.theta, self.phi, self.lam])

class CXGate(U3Gate):
    def to_pulse(self, vendor):
      if vendor == "Acme": 
        return Pulse.from_gate_parmas([self.theta, self.phi, self.lam])
      if vendor == "IBM":
        return Pulse.from_gate_parmas([self.theta, self.phi, self.lam])
      if vendor == "ZI":
        return Pulse.from_gate_parmas([self.theta, self.phi, self.lam])

class IDGate(U3Gate):
    def to_pulse(self, vendor): 
      if vendor == "Acme": 
        return Pulse.from_gate_parmas([self.theta, self.phi, self.lam])
      if vendor == "IBM":
          return Pulse.from_gate_parmas([self.theta, self.phi, self.lam])
      if vendor == "ZI":
          return Pulse.from_gate_parmas([self.theta, self.phi, self.lam])

class Measurement:
    def to_pulse(self, vendor):
      if vendor == "Acme": 
        return Pulse(0.1)
      if vendor == "IBM":
        return Pulse(0.2)
      if vendor == "ZI":
        return Pulse(0.3)

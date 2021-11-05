
class Pulse:
  def __init__(self, amp=0.0, freq=0.0):
      self.amp = amp
      self.freq = freq

  def from_gate_parmas(params): 
      # TODO: Do the transformation from gate angles to pulse params
      return params[0]  # Invent

  def from_params_to_freq(params):
      # TODO: Do the transformation from gate angles to pulse params
      return params[1] * params[2]  # Invent

pulse = Pulse()
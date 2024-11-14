# source: https://www.youtube.com/watch?v=oJyf8Q0KLRY
# title: Queuing System Discrete Event Simulation in Python (Event-scheduling)
import numpy as np

class Simulation:
  def __init__(self):
    self.num_in_system = 0
    
    self.clock = 0.0
    self.t_arrival = self.generate_interarrival()
    self.t_depart = float('inf')
    
    self.num_arrivals = 0
    self.num_departs = 0
    self.total_wait = 0.0
    
  def advance_time(self):
    t_event = min(self.t_arrival, self.t_depart)
    self.total_wait += self.num_in_system*(t_event - self.clock)
    self.clock = t_event
    
    if self.t_arrival <= self.t_depart:
      self.handle_arrival_event()
    else:
      self.handle_depart_event()
    
    print(f"num. of arrivals: {self.num_arrivals}, num. of departs: {self.num_departs}\n")
  
  def handle_arrival_event(self):
    self.num_in_system += 1
    self.num_arrivals += 1
    if self.num_in_system <= 1:
      self.t_depart = self.clock + self.generate_service()
    self.t_arrival = self.clock + self.generate_interarrival()
    
    print(f"num_in_system: {self.num_in_system}, t_arrival: {self.t_arrival}")
  
  def handle_depart_event(self):
    self.num_in_system -= 1
    self.num_departs += 1
    if self.num_in_system > 0:
      self.t_depart = self.clock + self.generate_service()
    else:
      self.t_depart = float('inf')
    
    print(f"num_in_system: {self.num_in_system}, t_depart: {self.t_depart}")
  
  def generate_interarrival(self):
    return np.random.exponential(1./3)
  
  def generate_service(self):
    return np.random.exponential(1./4)

np.random.seed(0)  
s = Simulation()

for i in range(100):
  s.advance_time()
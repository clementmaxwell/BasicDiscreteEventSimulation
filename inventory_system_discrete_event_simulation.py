# source: https://www.youtube.com/watch?v=7LuN_6m7h2o&t=740s
# title: Inventory System Discrete Event Simulation in Python (Event-scheduling)
import numpy as np

class Simulation:
  def __init__(self, order_cutoff, order_target):
    self.inventory = order_target
    self.num_ordered = 0
    
    self.clock = 0.0
    self.t_customer = self.generate_interarrival()
    self.t_delivery = float('inf')
    
    self.revenue = 0
    self.cost_orders = 0
    self.cost_holding = 0
    
    self.order_cutoff = order_cutoff
    self.order_target = order_target
    
  def advance_time(self):
    t_event = min(self.t_customer, self.t_delivery)
    self.cost_holding += self.inventory*2*(t_event - self.clock)
    self.clock = t_event
    
    if self.t_delivery <= self.t_customer:
      self.handle_delivery_event()
    else:
      self.handle_customer_event()
    
    print(f"Revenue: {self.revenue}, Cost Orders: {self.cost_orders}, Cost Holding: {self.cost_holding} \n")
  
  def handle_customer_event(self):
    demand = self.generate_demand()
    if self.inventory > demand:
      self.revenue += 100*demand
      self.inventory -= demand
    else:
      self.revenue += 100*self.inventory
      self.inventory = 0
    
    if self.inventory < self.order_cutoff and self.num_ordered == 0:
      self.num_ordered = self.order_target - self.inventory
      self.cost_orders += 50*self.num_ordered
      self.t_delivery = self.clock + 2
    
    self.t_customer = self.clock + self.generate_interarrival()
    
    print(f"inventory: {self.inventory}, t_customer: {self.t_customer}")
  
  def handle_delivery_event(self):
    self.inventory += self.num_ordered
    self.num_ordered = 0
    self.t_delivery = float('inf')
    
    print(f"num_in_system: {self.num_in_system}, t_delivery: {self.t_delivery}")
  
  def generate_interarrival(self):
    return np.random.exponential(1./5)
  
  def generate_demand(self):
    return np.random.exponential(1./5)

np.random.seed(0)  
s = Simulation(10, 30)

while s.clock <= 2.0:
  print(f'clock: {s.clock}')
  s.advance_time()
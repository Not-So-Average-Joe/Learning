def ground_shipping(weight):
  if weight <= 2:
    cost = weight * 1.50 + 20.00
    return cost
  elif weight > 2 and weight <= 6:
    cost = weight * 3.00 + 20.00
    return cost
  elif weight > 6 and weight <= 10:
    cost = weight * 4.00 + 20.00
    return cost
  else:
    cost = weight * 4.75 + 20.00
    return cost

premium_shipping = 125.00

#print(ground_shipping(8.4))  

def drone_shipping(weight):
  if weight <= 2:
    cost = weight * 4.50 
    return cost
  elif weight > 2 and weight <= 6:
    cost = weight * 9.00
    return cost
  elif weight > 6 and weight <= 10:
    cost = weight * 12
    return cost
  else:
    cost = weight * 14.25
    return cost
  
#print(drone_shipping(1.5))

def cheapest_shipping_method(weight):
  if ground_shipping(weight) < drone_shipping(weight) and ground_shipping(weight) < premium_shipping:
    return "You should use ground shipping, it will cost £" + str(ground_shipping(weight))
  elif drone_shipping(weight) < ground_shipping(weight) and drone_shipping < premium_shipping:
    return "You should use drone shipping, it will cost £" + str(drone_shipping(weight))
  else:
    return "You should use premium shipping, it will cost £" + str(premium_shipping)
    
print(cheapest_shipping_method(4.8))
print(cheapest_shipping_method(41.5))  
  
  
  

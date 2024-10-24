# write a unique random numbers function 

import random

def get_numbers_ticket(min, max, quantity):
  # check input parameters are correct
  if min < 1 or max > 1000 or quantity > (max - min + 1) or quantity <= 0:
    return[]
  
  # generate unique random numbers
  lottery_numbers = random.sample(range(min, max +1), quantity)

  # return sorted list
  return sorted(lottery_numbers)

# use case
lottery_numbers = get_numbers_ticket(1, 100, 7)
print("Your lottery numbers:", lottery_numbers)
"""
Module to create and check EAN13 numbers.
Otra parte.
"""

# Imported libraries
import random

# Defined classes

class Code:
  # Class Variable
  # animal = 'dog'
  # The init method or constructor
  def __init__(self, code):
  # Instance Variable
    self.code = code
  # Adds an instance variable
  def set_digit(self, ind, digit):
    if ind >= 13:
      print("not possible to change the check digit.")
    else:
      inter = self.code[:ind-1] + str(digit) + self.code[ind:]
      odd = sum([int(inter[i]) for i in range(len(inter)-1) if i%2 == 0])
      even = 3 * sum([int(inter[i]) for i in range(len(inter)) if i%2 == 1])
      cd = str(10 - (odd + even) % 10)
      self.code = inter[:-1] + cd
  # Retrieves instance variable
  def get_checkdigit(self):
    return self.code[-1]
  # Retrieves instance variable
  def get_infodigit(self):
    return self.code[:-1]
  # Check if ean
  def ean(self):
    """
    Function that checks if a sequence of 13 digits is a correct ean13
    number.
    """
    if len(self.code) != 13:
      return False
    else:
      odd = sum([int(self.code[i]) for i in range(len(self.code)-1) if i%2 == 0])
      even = 3 * sum([int(self.code[i]) for i in range(len(self.code)) if i%2 == 1])
      cd = str(10 - (odd + even) % 10)
      if cd == self.code[-1]:
       return True
      else:
       return False



# Defined functions

def check_digit(digits):
  """
  Computes the check digit from a sequence of 12 digits.
  """
  odd = sum([int(digits[i]) for i in range(len(digits)-1) if i%2 == 0])
  even = 3 * sum([int(digits[i]) for i in range(len(digits)) if i%2 == 1])
  cd = 10 - (odd + even) % 10
  return str(cd)

def rand_ean_num():
  """
  Function that creates a random ean13 number.
  """
  sal = ''.join([str(random.randint(0, 9)) for i in range(12)])
  cd = check_digit(sal)
  sal = sal + cd
  return sal

def rand_nean_num():
  """
  Function that creates a random ean13 number.
  """
  sal = ''.join([str(random.randint(0, 9)) for i in range(12)])
  cd = check_digit(sal)
  eq = True
  while eq:
    cdr = str(random.randint(0, 9))
    if cdr != cd:
      cd = cdr
      eq = False
  sal = sal + cd
  return sal

def check_ean(digits):
  """
  Function that checks if a sequence of 13 digits is a correct ean13
  number.
  """
  if len(digits) != 13:
    return False
  else:
    if check_digit(digits[:12]) == digits[-1]:
      return True
    else:
      return False




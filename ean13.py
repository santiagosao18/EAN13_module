"""
Module to create and check EAN13 numbers.
Otra parte.
"""

# Imported libraries
import random

# Defined classes

class Foo:
    """Help for the class Foo"""

    def bar(self):
        """Help for the bar method of Foo classes"""

def spam(f):
    """Help for the spam function"""

def greeting(name):
  print("Hello, " + name)


# Defined functions

def check_digit(digits):
  """
  Computes the check digit from a sequence of 12 digits.
  """
  odd = sum([int(digits[i]) for i in range(len(digits)-1) if i%2 == 0])
  even = 3 * sum([int(digits[i]) for i in range(len(digits)) if i%2 == 1])
  cd = 10 - (odd + even) % 10
  return str(cd)

def rand_num():
  """
  Function that creates a random ean13 number.
  """
  sal = ''.join([str(random.randint(0, 9)) for i in range(12)])
  cd = check_digit(sal)
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




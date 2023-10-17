"""
Module to create and check EAN13 numbers.
Otra parte.
"""
import random

class Foo:
    """Help for the class Foo"""

    def bar(self):
        """Help for the bar method of Foo classes"""

def spam(f):
    """Help for the spam function"""

def greeting(name):
  print("Hello, " + name)

def rand_num():
  """
  Function that creates a random ean13 number.
  """
  sal = ''.join([str(random.randint(0, 9)) for i in range(12)])
  return sal

def check_digit(digits):
  odd = sum([int(digits[i]) for i in range(len(digits)-1) if i%2 == 0])
  even = 3 * sum([int(digits[i]) for i in range(len(digits)) if i%2 == 1])
  cd = 10 - (odd + even) % 10
  return str(cd), even, odd

def check_ean(digits):
  cd = '0'
  return cd
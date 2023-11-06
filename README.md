# EAN13_module
A Python module to create and manipulate code numbers through the EAN-13 standard. 

## 1) Code numbers with the EAN-13 standard

The 13-digit EAN-13 number consists of two main components. The first 12 digits (which in turn can be divided in three groups: 
the GS1 prefix, the manufacturer code and the product code) contain information about a product. The last digit is a verfication 
digit computed from the first 12 digits using a specific formula (you can learn about this in 
[Wikipedia](https://en.wikipedia.org/wiki/International_Article_Number#:~:text=The%20most%20commonly%20used%20EAN,or%20special%20type%20of%20product)
and 
[this site](https://boxshot.com/barcode/tutorials/ean-13-calculator/)).

## 2) The module

This is a simple module with four functions and one defined class.

### 2.1) The functions

The check_digit(digits) function takes a sequence of 12 digits and returns the verification digit.
The rand_ean_num() creates a random number according to the EAN-13 standard (that is, the verification digit is the correct digit for the 12 first digits).
The rand_nean_num() creates a random number that does not follows the EAN-13 standard (that is, the verification digit is not the correct digit for the 12 first digits).
The check_ean(digits) checks if a sequence of 13 digits is a good EAN-13 number. Returns True or False.

### 2.2) The Code class

The set_digit method(ind, digit) permits changing the value of a given digit (other than the verification digit) at position ind (between 1 and 12) with the new value digit.
The get_checkdigit method returns the verification digit (the last digit of the code).
The get_infodigit method returns the information digits (the first 12 digits of the code).
The ean method checks if a given code is a correct EAN-13 number.
The correct method corrects de verification digit.

## 3) Examples
1234567890128

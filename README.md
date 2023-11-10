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

You can find here a series of examples that show how each function, object and method works.

### 3.1) Examples using the functions

The number 4007817502259 is a correct EAN-13 number, where 9 is the verification digit.

If you compute: <br/>
`check_digit('400781750225') >>> '9'`


You can create randon EAN-13 numbers:<br/>
`rand_ean_num() >>> '9704566317602'`


If you compute: <br/>
`check_digit('970456631760') >>> '2'`


You can also create randon numbers that does not satisfy the EAN-13 standard:<br/>
`rand_nean_num() >>> '8427672846691'` <br/>
which is not an EAN-13 number since the verification digit should be 9 instead of 1 <br/>
`check_digit('842767284669') >>> '9'`

With the function check_ean(digits) you can check if a sequence of 13 digits is a correct EAN-13 number:<br/>
`check_ean('4007817502259') >>> True`<br/>
`check_ean('4007817502258') >>> False`<br/>
`check_ean('9704566317602') >>> True`<br/>
`check_ean('8427672846691') >>> False`<br/>
`check_ean('8427672846699') >>> True`

### 3.2) Examples using the Code class and its methods

With the Code class it is possible to create a number with 13 digits.
This number could be or not a correct EAN-13 number. The Code class has a single attribute, the 'code' attribute that stores the code number.
The class contains a number of methods to check if the code is a correct a EAN-13 number or not. It is possible to correct the verification digit
and to modify a specific digit (within the first 12 digits in the sequence) that will change not only the selected digit, but also the verification
digit to be consistent with the new digit.

Here are some exmples. The number 1234567890128 is a correct EAN-13 number.

Create a EAN-13 number and extract the verification digit and the information digits:

`cn = Code('1234567890128')`<br/>
`cn.get_checkdigit() >>> 8`<br/>
`cn.get_infodigit() >>> 123456789012`

Create a 13 digit code and verify if it corresponds to an EAN-13 number or not:

`cn = Code('1234567890128')`<br/>
`cn.ean() >>> True`<br/>
`cn = Code('1234567890129')`<br/>
`cn.ean() >>> False`

Change a digit at a specific position. In the example below the first digit is changed by 2, and also the verification
digit is automatically changed to the correct value which is 7:<br/>
`cn = Code('1234567890128')`<br/>
`cn.set_digit(1,2)`<br/>
`cn.code >>> 2234567890127`

If the code is not a correct EAN-13 number, calling the correct method is possible to modify the code number: the method keeps
the first 12 digits in its original form but modifies the verification digit to the correct value <br/>
`cn = Code('1234567890129')`<br/>
`cn.code >>> '1234567890129'`<br/>
`cn.correct()`<br/>
`cn.code >>> '1234567890128'`

Naturally, applying the correct() method to a correct EAN-13 number does nothing:<br/>
`cn = Code('1234567890128')`<br/>
`cn.code >>> '1234567890128'`<br/>
`cn.correct()`<br/>
`cn.code >>> '1234567890128'`

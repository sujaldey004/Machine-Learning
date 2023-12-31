# -*- coding: utf-8 -*-
"""first code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X7khJGMtMKyZJAgs8C6MhW6kzAv_VPuz

"random" library is used to generate random numbers and sequences.
This library contains many function like this.
"""

import random

"""In this cell we are creating a dictionary which map the numbers 0-9 to the characters 0-9.
This in done with zip() function. Zip function takes two iterable and returns a list of tuple.
We are zipping the element 0-9 with the character 0-9.
"""

mapping_dict = dict(zip(range(0,10),range(48,58)))
for k in mapping_dict.keys():
  mapping_dict[k] = chr(mapping_dict[k])

"""Printing the Dictionary which contain list of tuples.
For loop is used to go over the keys and assign the values.
"""

mapping_dict

"""Here we are assigning the character A to Key 10 with the help of chr() function.


"""

mapping_dict[10] = chr(65)

"""Printing the dictionary from o to 10."""

mapping_dict

"""Here we are using for loop to iterate over 0-25 and assign the corresponding latters to the number.
"10+i" and "65+i" means "10+(0-25)" and "65+(0-25)"
"""

for i in range(0,26):
  mapping_dict[10+i] = chr(65+i)

"""Printing the dictionary from 0-35 keys and character 0-9 and A-Z"""

mapping_dict

"""First we are creating a blank string.
For loop iterates over the numbers 0-8 and assigns the value of each number to the variable i.
Generating a random number between 0 and 1,done using the random.randint() function.
Checking if the random number is equal to 1.
Generating a random number between 0 and 35.
Then we are appending and concatinating two character corresponding to generated two random number and store it in blank string
"""

blank_str = str()

random_digit = random.randint(0,35)
blank_str = blank_str + mapping_dict[random_digit]

random_digit = random.randint(0,35)
blank_str = blank_str + mapping_dict[random_digit]

for i in range(0,8):
  coin_toss = random.randint(0,1)
  if coin_toss == 1:
    random_digit = random.randint(0,35)
    blank_str = blank_str + mapping_dict[random_digit]
  else:
   break

"""Printing the blank string"""

blank_str

"""Creating a new dictionary.
we are passing the mapping dictionary as the sequence of key-value pairs.
The for loop iterates over the keys of the dictionary and assigns the value of each key to the variable k.
Assigning the key of the mapping dictionary to the value of the new dictionary.

"""

new_dict = dict()
for k in mapping_dict:
  new_dict[mapping_dict[k]] = k

"""Printing new dictionary"""

new_dict

"""Finding the highest digit in the blank string using the max() function which takes a sequence of numbers and returns the largest number in the sequence, we are passing blank string to the max finction.
Finding the base of the highest digit in the blank string by using the new dictionary and adding 1 to it. The new dictionary maps the characters to the numbers.
Then printing the blank string and the Highest base
"""

highest_digit = max(blank_str)
highest_base = new_dict[highest_digit] + 1
print("Highest Base of {} is {}".format(blank_str,highest_base))
#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
    digit = -digit
    print("Last digit of {} is {} and is".format(number,digit))
if digit > 5:
    print("Last digit of 98 is 8 and is greater than 5")
elif digit == 0:
    print("Last digit of 0 is 0 and is 0")
else:
    print("Last digit of -98 is -8 and is less than 6 and not 0")

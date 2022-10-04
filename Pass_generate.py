# generate password which is tough to break for

import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "!@#$%&*?"

string = lower + upper + number + symbols
length = 8
password = "".join(random.sample(string, length))

print("Your Generated Password is:" + password)

# creating a random password generator with the options
import sys
import random

lenght_of_pass = sys.argv[1]
print(f"you have selected length for password is = {lenght_of_pass}" )

res = []
for i in range(int(lenght_of_pass)):   # i is going to iterate and length of pass is getting value from the cmd line also it needs to convert as its string to int
    randop =  random.randrange(0,9)   # random.randrange(0,9) getting random number from range of 0 to 9  
    res.append(randop)          # Need a loop to get the random number range it to that length

output = ''.join(map(str, res))  # empty strin '' with join function to map the str of all the res array 
print(output) # prininting output
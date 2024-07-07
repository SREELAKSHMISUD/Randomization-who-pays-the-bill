# example of random function for head or tails
#import random
# random_side = random.randint(0, 1)
# if random_side == 1:
#   print("Heads")
# else:
#   print("Tails")

import random
names_string= "Angel,Ceasar,Ben,Jane, Alex, Emily, Chris"
names=names_string.split(", ")
#to get total number of items in list
num_items=len(names)
#generate random numbers between 0 and last index
random_choice=random.randint(0,num_items-1)
#choose and print random name
print(names[random_choice]+ " is going to buy the meal today!")
import random


"""
If I don't define any seed using random.seed, Python will get an interval value from the computer base on current time in miliseconds.
"""

def six_sides():
    dice = random.randint(1, 6)
    print(dice)

def four_sides(): 
    dice = random.randint(1, 4)
    print(dice)

def eight_sides():
    dice = random.randint(1, 8)
    print(dice)

def twelve_sides():
    dice = random.randint(1, 12)
    print(dice)

def twenty_sides():
    dice = random.randint(1, 20)
    print(dice)





def main():
    four_sides()
    six_sides()
    eight_sides()
    twelve_sides()
    twenty_sides()



if __name__ == "__main__":
    main()




#OTHER CONSIDERATIONS


"""
using seed:  a fixed seed will alway output the same result

random.seed(42)
print(random.randint(1, 100))  # Outputs: 82


# ***The seed is the starting value: It is the initial number fed into the computer's mathematical equation to kick off the calculations.
# ***Changing the seed changes the output: If you switch from random.seed(42) to random.seed(99), you plug a new number into the equation, which completely changes the resulting sequence of numbers.
# ***randint is just the range: random.randint(a, b) simply sets the boundaries (the minimum and maximum allowed limits) for the number that the math equation spits out.

"""






"""
Other way to use
> Creating an objetc instance generator and passing the sedd directly in the cosntructor creating independent objects instead of a global ("random" word in random.randint() is a global)

from random import Random

generator = Random(34)
print(generator.randint(1, 10))

"""







"""
In data science the modern recomendation is: 

import numpy as np
rng = np.random.default_rng(seed=42)
print(rng.integers(1, 100))
"""






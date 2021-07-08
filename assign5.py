# 1) Import the random function and generate both a random number between 0 and 1 as well as a random number between 1 and 10.

import random
import datetime

random_number = random.randrange(1, 10)
random_number_flt = random.random()

# 2) Use the datetime library together with the random number to generate a random, unique value.

time_stamp = datetime.datetime.now()
unique_value = '{}-{}'.format(str(random_number), str(time_stamp))
print('Random number between 1 and 10 : {}'.format(random_number))
print('Random number between 0 and 1 : {}'.format(random_number_flt))
print('Unique value using current timestamp : {}'.format(unique_value))

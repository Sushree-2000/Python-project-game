'''
# 4 - How to Get the Current Username in Python
import os
import getpass

try:
    username = os.getlogin()
except OSError:
    username = getpass.getuser()

print(username)


# 5 - How to access environment variables in Python
import os

for key, value in os.environ.items():
    print(f"{key} = {value}")



# 6 - How to do a profile a Python script
import cProfile

def my_function():
    total = 0
    for i in range(1000000):
        total += i
    print(total)

cProfile.run('my_function()')
'''




# 7 - How to List all Files of a Directory in Python
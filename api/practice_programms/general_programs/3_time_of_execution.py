# 3 - How to get time of a Python program's execution
import random
import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        self.progSome()
        return self
    def progSome(self):
        a = random.random()
        b = random.random()
        print(f"sum of 2 random numbers {a} and {b} = {a+b}")
    def __exit__(self, *args):
        self.end = time.time()
        print("Execution time:", self.end - self.start, "seconds")

with Timer():
    for _ in range(1000000):
        pass

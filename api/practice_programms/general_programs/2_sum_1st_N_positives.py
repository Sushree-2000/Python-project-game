# 2 - How to Sum of the First N Positive Integers in Python

class Sum1stNPositiveNums:
    def __init__(self):
        # pass
        self.nums = list(map(int, input("Enter any random numbers separated by commas = ").split(',')))
        self.n = input(f"Enter the number you want to take that much of positive number. \nGiven input should be less than the number of provided inputs(< {len(self.nums)}). = ")
        self.sumPosN()
    def sumPosN(self):
        num_arr = self.nums
        n = int(self.n)
        sums, cnt = 0, 0
        pos_nums = []
        # sumsn = [sums+=i for i in range(len(num_arr)) if]
        for i in range(len(num_arr)):
            if (num_arr[i]%2 == 0 and cnt < n):
                sums+=num_arr[i]
                cnt+=1
                pos_nums.append(num_arr[i])
        print(f"Sum of {n} postive numbers from the inputs {','.join(map(str, num_arr))} is \n: {'+'.join(map(str, pos_nums))} = {sums}")

obj = Sum1stNPositiveNums()
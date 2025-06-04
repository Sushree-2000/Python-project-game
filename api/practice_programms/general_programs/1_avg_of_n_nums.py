'''# 1 - How to find average of N numbers in Python (Type-1)
class AvgOfNum:
  def __init__(self):
    # self.n = n
    self.length = int(input("Enter the count of numbers u want average for: "))
    self.avgCalc(self.length)
  def avgCalc(self, lists):
    self.lists = list(map(int, input(f"Enter {self.length} numbers seprated by comma to calculate your average: ").split(',')))
    if(len(self.lists) != self.length):
      print(f"Provide exactly {self.length} number of inputs.")
      # self.enterList(self.length)
    else:
      total_sum = 0
      for i in self.lists:
        total_sum+=i
      avrg = total_sum/self.length
      print(f"Average of {','.join(map(str, self.lists))} = {avrg}")
    # print(length)

obj1 = AvgOfNum()

# 1 - How to find average of N numbers in Python (Type-2)
class AvgOfNum:
  def __init__(self):
    # self.n = n
    self.length = int(input("Enter the count of numbers u want average for: "))
    self.enterList(self.length)
  def enterList(self, length):
    self.length = length
    self.lists = list(map(int, input(f"Enter {length} numbers seprated by comma to calculate your average: ").split(',')))
    while len(self.lists) != self.length:
      if(len(self.lists) > self.length):
        print(f"{self.lists}. Please remove {len(self.lists)-self.length} numbers, you have given more than required inputs.")
        self.lists = list(map(int, input().split(',')))
      elif(len(self.lists) < self.length):
        print(f"{self.lists}. Please add {self.length - len(self.lists)} more numbers, you have given less than required inputs.")
        self.lists = list(map(int, input("Enter the numbers: ").split(',')))
    self.avgCalc(self.lists)

  def avgCalc(self, lists):
    if(len(lists) != self.length):
      print(f"Provide exactly {self.length} number of inputs.")
      self.enterList(self.length)
    else:
      total_sum = 0
      for i in self.lists:
        total_sum+=i
      avrg = total_sum/self.length
      print(f"Average of {','.join(map(str, self.lists))} = {avrg}")

obj1 = AvgOfNum()
'''


# 1 - How to find average of N numbers in Python (Type 3)
class AvgOfNum:
  def __init__(self):
    self.lists = list(map(int, input(f"Enter the numbers seprated by comma to calculate average: ").split(',')))
    self.avgCalc(self.lists)
  def avgCalc(self, lists):
    total_sum = 0
    for i in self.lists:
        total_sum+=i
    avrg = total_sum/len(self.lists)
    print(f"Average of {','.join(map(str, self.lists))} = {avrg}")

obj1 = AvgOfNum()


















'''

number_count = int(input("Enter Count :" ))
print(f"Count: {number_count}")

i = 1
sum = 0
average = 0
while i <= number_count:
    number = int(input("Enter the Number :" ))
    print(f"Number - {i} : {number}")
    sum = sum + number
    i = i + 1
else:
    average = sum/number_count

print(f"\nSum: {sum}")
print(f"Average: {round(average, 2)}")




number_count = int(input("Enter how many numbers you want to input: "))
print(f"Count: {number_count}")

total = 0

for i in range(1, number_count + 1):
    number = int(input(f"Enter number {i}: "))
    print(f"number - {i} : {number}")

    total += number

average = total / number_count

print(f"\nSum: {total}")
print(f"Average: {round(average, 2)}")




numbers = input("Enter input in comma-separated format: ")
print(f"Given Input: {numbers}")

raw_inputs = numbers.split(",")

total = 0
count = 0
valid_numbers = []

for num in raw_inputs:
    cleaned = num.strip()  #remove space
    try:
        value = float(cleaned)
        total += value
        count += 1
        valid_numbers.append(cleaned)
    except ValueError:
        print(f"⚠️ '{cleaned}' is not a valid number and will be skipped.")

if count == 0:
    print("\n❌ No valid numbers were entered.")
else:
    average = total / count
    print(f"\n✅ Valid Numbers: {valid_numbers}")
    print(f"✅ Sum: {total}")
    print(f"✅ Average: {round(average, 2)}")
'''

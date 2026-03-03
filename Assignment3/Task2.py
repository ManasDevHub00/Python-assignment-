import math

# 1. Take input from user
num = float(input("Enter a number: "))

# 2. Calculate values using math module
square_root = math.sqrt(num)
natural_log = math.log(num)
sine_value = math.sin(num)

# 3. Display results
print("Square Root:", square_root)
print("Natural Logarithm (log base e):", natural_log)
print("Sine (in radians):", sine_value)
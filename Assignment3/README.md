# 📘 Python Tasks README

## 📌 Project Title

**Factorial Calculator and Mathematical Operations using Python**

---

## 🧾 Description

This project contains two Python programs:

1. **Factorial calculation using a recursive function**
2. **Mathematical calculations using the `math` module**

These programs demonstrate basic Python concepts such as user input, functions, recursion, and built-in modules.

---

## ✅ Task 1: Factorial Using Function

### 🎯 Objective

Write a Python program that calculates the factorial of a number using a recursive function.

### 📖 Definition

Factorial of a number **n** is:

```python
n! = n × (n-1) × (n-2) × ... × 1
```

Example:

```python
5! = 120
```

### 💻 Program Code

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number to calculate its factorial: "))
result = factorial(num)

print("Factorial =", result)
```

### ▶️ Example Output

```python
Enter a number to calculate its factorial: 5
Factorial = 120
```

---

## ✅ Task 2: Mathematical Calculations

### 🎯 Objective

Create a Python program that:

* Accepts a number from the user.
* Calculates:

  * Square Root
  * Natural Logarithm (log base *e*)
  * Sine value (in radians)
* Displays the calculated results.

### 💻 Program Code

```python
import math

# Take input from user
num = float(input("Enter a number: "))

# Perform calculations
square_root = math.sqrt(num)
natural_log = math.log(num)
sine_value = math.sin(num)

# Display results
print("Square Root:", square_root)
print("Natural Logarithm (log base e):", natural_log)
print("Sine (in radians):", sine_value)
```

### ▶️ Example Output

```python
Enter a number: 16
Square Root: 4.0
Natural Logarithm (log base e): 2.77
Sine (in radians): -0.2879
```

---

## 🚀 How to Run the Program

1. Install Python on your system.
2. Save the file as:

```python
program.py
```

3. Open terminal or command prompt.
4. Run the program:

```python
python program.py
```

---

## 📚 Concepts Learned

* Python user input and output
* Functions in Python
* Recursion
* Using the `math` module
* Basic mathematical operations

---

## 👨‍💻 Author

**Manas Sharma**

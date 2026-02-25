# Python Basic Tasks – User Input & Operations

## 📌 Overview

This repository contains two beginner-level Python programs designed to practice **user input**, **string handling**, and **basic mathematical operations**.

---

## ✅ Task 1: Basic Mathematical Operations

### 🎯 Objective

Create a Python program that:

* Takes two numbers as input from the user.
* Performs:

  * Addition
  * Subtraction
  * Multiplication
  * Division
* Displays the result of each operation.

### 💻 Program

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
    division = "Division not possible"

print("\nResults:")
print("Addition =", addition)
print("Subtraction =", subtraction)
print("Multiplication =", multiplication)
print("Division =", division)
```

### ▶ Example Output

```
Enter first number: 10
Enter second number: 5

Results:
Addition = 15.0
Subtraction = 5.0
Multiplication = 50.0
Division = 2.0
```

---

## ✅ Task 2: Personalized Greeting Program

### 🎯 Objective

Create a Python program that:

* Takes user's first name and last name.
* Combines them into a full name.
* Displays a personalized greeting message.

### 💻 Program

```python
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print(f"Hello {first_name} {last_name} Welcome")
```

### ▶ Example Output

```
Enter your first name: Manas
Enter your last name: Sharma
Hello Manas Sharma Welcome
```

---

## 🛠 Technologies Used

* Python 3
* VS Code / Any Python IDE

---

## 📚 Learning Outcomes

* Taking user input
* Using variables
* Performing arithmetic operations
* String concatenation
* Using f-strings in Python

---

## 👨‍💻 Author

**Manas Sharma**

---

⭐ Beginner Python Practice Tasks

# Simple Calculator using Tkinter

## Overview

This project is a basic calculator application built using Python's Tkinter library. It provides a graphical user interface (GUI) that allows users to perform simple arithmetic operations such as addition, subtraction, multiplication, and division.

## Features

* User-friendly GUI
* Addition (+)
* Subtraction (-)
* Multiplication (*)
* Division (/)
* Clear button (C)
* Error handling for division by zero

## Technologies Used

* Python 3
* Tkinter (built-in Python GUI library)

## Project Structure

```
calculator.py
README.md
```

## How It Works

1. Enter the first number using the number buttons.
2. Select an arithmetic operation (+, -, *, /).
3. Enter the second number.
4. Press the "=" button to display the result.
5. Press the "C" button to clear the display.

## Functions Used

### click(num)

Displays the clicked number in the entry box.

### add()

Stores the first number and prepares for addition.

### sub()

Stores the first number and prepares for subtraction.

### mul()

Stores the first number and prepares for multiplication.

### div()

Stores the first number and prepares for division.

### equal()

Performs the selected arithmetic operation and displays the result.

### clear()

Clears the calculator display.

## Installation

1. Make sure Python 3 is installed.
2. Clone or download this repository.
3. Run the program:

```bash
python calculator.py
```

## Example

```
Input: 12 + 8
Output: 20

Input: 15 * 4
Output: 60

Input: 10 / 0
Output: Error
```

## Future Improvements

* Support decimal numbers
* Add keyboard input support
* Improve UI using grid layout
* Add advanced operations (%, square root, power)
* Add calculation history

## Author

Manas Sharma

## License

This project is open-source and available for learning and educational purposes.

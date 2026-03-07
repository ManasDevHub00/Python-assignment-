# Task 1: Read a File and Handle Errors 

try:
    with open("Assignment4/Sample.txt","r") as f:
        for line in f:
            print(line.strip())
except FileNotFoundError as e:
    print("The file 'Assignment4/Sample.txt' was not found. Please check the file name and try again.")
    print(f"Error details: {e}")
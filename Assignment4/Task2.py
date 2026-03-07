# 1. Take user input and write to file
data = input("Enter some text: ")

file = open("output.txt", "w")
file.write(data + "\n")
file.close()

# 2. Append additional data
more_data = input("Enter more text to append: ")

file = open("output.txt", "a")
file.write(more_data + "\n")
file.close()

# 3. Read and display final content
file = open("output.txt", "r")

print("\nFinal content of the file:")
for line in file:
    print(line.strip())

file.close()
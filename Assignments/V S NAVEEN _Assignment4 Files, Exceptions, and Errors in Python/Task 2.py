# Task 2: Write and Append Data to a File

# Take user input
data = input("Enter some text to write to the file: ")

# Write data to the file
with open("output.txt", "w") as file:
    file.write(data + "\n")

print("Data successfully written to output.txt.")

# Take additional input
additional_data = input("Enter additional text to append: ")

# Append data to the same file
with open("output.txt", "a") as file:
    file.write(additional_data + "\n")

print("Data successfully appended.")

# Read and display final content
print("\nFinal content of output.txt:")

with open("output.txt", "r") as file:
    content = file.read()
    print(content)
#task1 - creates a sample.txt file tries to open and handles the error
with open('sample.txt', 'w') as file:
    file.write("Hello! This is the first line.\n")
    file.write("Python file handling is easy.\n")
    file.write("Dont forget to close your file")

try:
    # attempt to open and read the file
    with open('sample.txt', 'r') as file:
        print("file Content")
        for line in file:
            # .strip() to remove extra newlines from the file
            print(line.strip())

except FileNotFoundError:
    #handle the error if the file is missing
    print("Error: The file 'sample.txt' was not found.")
    print("Please make sure the file exists in the same folder as your script.")


#Task 2- creates a output.txt file with 1st input and appends 2nd input from user and displays final content
input1=input("Please enter your first input to append to file : ")
with open('output.txt','w') as file:
    file.write(input1+"\n")
input2=input("Please enter your second input to append to file : ")
with open('output.txt','a') as file:
    file.write(input2+"\n")
with open("output.txt","r") as file:
    content=file.read()
    print(content)

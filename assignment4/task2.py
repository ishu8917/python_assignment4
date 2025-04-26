# Task 2: Write and Append Data to a File

filename= "Output.txt"

with open(filename,'a+') as file:
    writting_file=file.write("Hello, Python!"+"\n")
    file.seek(0)
    content=file.read()
    print("Enter the text to write in the file:",content)
    print(f"Data is successfully written in file {filename}\n")


with open("output.txt", "a+") as file:
    file.write("Learnig the file handling in Python" + "\n")

with open('output.txt', 'r') as file:
    lines = file.readlines()  # read all lines into a list

if len(lines) >= 2:
    print("Enter the additional text to append:",lines[1].strip())  
    print("Data Successfully appended")



print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)
    


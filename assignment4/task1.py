# Task 1: Read a File and Handle Errors

filename="Sample.txt"

try:
   with open(filename,"r") as file:
       reading_file = file.read()
       print("Reading file comtent:\n",reading_file)
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found")

except Exception as e:
    print(f"An unexpected error occured: {e}")

finally:
    print("Continue further....")



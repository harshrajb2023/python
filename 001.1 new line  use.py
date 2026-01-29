
print("Hello\nWorld")






print(" \n ") // Spaces printed
   #vs
print("vs")
print("\n")  // spaces not printed


name = "Alice"
age = 25
print(f"Name: {name}\nAge: {age}")



with open("example.txt", "w") as file:
    file.write("First Line\nSecond Line\nThird Line")




#output
Explanation (quick & clear):
"w" → write mode (creates file if it doesn’t exist, clears it if it does)
\n → new line
with open(...) as file: → automatically closes the file after writing




lines = ["Line 1", "Line 2", "Line 3"]
result = "\n".join(lines)
print(result)



#Output
Line 1
Line 2
Line 3




for i in range(1, 4):
    print("Line {i}\n", end="")  # Avoids extra newlines

# wrong
Why?
"Line {i}" is just a normal string
Python does not replace {i} unless you tell it to
{i} is printed literally

    
       #vs
 
for i in range(1, 4):
    print(f"Line {i}\n", end="")  # Avoids extra newlines

# currect
Why?
f"..." is an f-string
{i} gets replaced with the value of i

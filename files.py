# File management

# Open file : open(filename, access, buffering)
filename = open("file_name.txt", "r")

# Read a file
print(filename.read())
# Read specific amount of characters
print(filename.read(20)) # NOTE : To use read again you need to get the cursor back to 0
filename.seek(0)

# Get the length of the file 
print(filename.tell())

# Move pointer seek(steps)
filename.seek(22) # Move cursor to the position 22
print(filename.tell())
filename.seek(0)

# Loop reading of a file
for line in filename:
    print (line)

# Close file
filename.close()

# Writing 
# w+ override the old file or create it
filename = open("file_name.txt", "w+")
filename.write("Hello, File!") # When writing the cursor moves to the end of the string so in or
filename.seek(0)
print("Writen file: {fileContent}".format(fileContent = filename.read()))

filename.close()

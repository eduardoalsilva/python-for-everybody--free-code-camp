fileContent = open('mbox-short.txt') # saves the file content to fileContent variable
print(fileContent) # prints the fileContent variable


# prints every line in upper case removing extra blank spaces
for line in fileContent: 
    lineUpper = line.rstrip()
    print(lineUpper.upper())

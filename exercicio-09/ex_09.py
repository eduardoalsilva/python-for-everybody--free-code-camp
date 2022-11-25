# save in a variable a value wrote by the user
# If the user doesn't write anything it saves the clown.txt file to fileName

fileName = input('Enter File: ')
if len(fileName) < 1:
    fileName = 'clown.txt'


# save the file content in handleContent

handleContent = open(fileName)


# create a dictionary type variable called counts
# delete extra spaces and split each line to a list variable called words

counts = dict( )
for line in handleContent:
    line = line.rstrip()
    words = line.split()
    for word in words: # counts how many the current word appears
        counts[word] = counts.get(word,0) + 1

    largest = -1
    theword = None
    for keys,values in counts.items(): # compares the dictionary keys to find which one has a higher value, which one appears more
        if values > largest:            # save the key and the value of the result to new variables
            largest = values
            theword = keys

# prints the word and how many time it appears

print('Done',theword, largest)

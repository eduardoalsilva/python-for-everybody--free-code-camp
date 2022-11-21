# open and save the mbox-short.txt content to a variable called openFile
openFile = open('mbox-short.txt')

# take every line in the text, delete the blank extra spaces and split the line in words, saving to the words list variable
# checks if the first word on the line is "From" and the word list is higher than 3. If yes it prints the third word in the line, that is the weekday
for line in openFile:
    line = line.rstrip()
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[2])

# Open the file the user types or clown.txt if he doesn't write anything and save in the content variable

fileName = input('Enter File: ')
if len(fileName) < 1:
    fileName = 'clown.txt'

content = open(fileName)

# creates a dictionary and save in keys and values to the counts dictionary, counting each one of them

counts = dict( )
for line in content:
    line = line.rstrip()
    words = line.split()
    for w in words:
        counts[w] = counts.get(w,0) + 1


# get the key and value and change position to value and key
        
tmp = list()
for key, value in counts.items():

    newTuple = (value,key)
    tmp.append(newTuple)


# sort the tmp list content and print inverting the position again to key and valyue
tmp = sorted(tmp, reverse=True)

for value,key in tmp[:5]:
    print(key,value)
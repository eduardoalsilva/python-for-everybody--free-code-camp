fileName = input('Enter File: ')
if len(fileName) < 1:
    fileName = 'clown.txt'

handleContent = open(fileName)

di = dict( )
for line in handleContent:
    line = line.rstrip()
    words = line.split()
    for w in words:
        di[w] = di.get(w,0) + 1

    largest = -1
    theword = None
    for k,v in di.items():
        if v > largest:
            largest = v
            theword = k

print('Done',theword, largest)

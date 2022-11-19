# line 3 save a string type to a variable called str

str = 'X-DSPAM-Confidence: 0.8475'

# line 8 save to the ipos variable the position of the character ":"
# line 9 prints which the position saved on ipos is

ipos = str.find(':')
print(ipos)

# line 14 save to piece variable the characters in str variable from the ipos position + 1 until the last position
# line 15 prints the piece variable value. Observe that the space after the numbers is also saved in the variable

piece = str[ipos+1:]
print(piece)

# line 20 saves the value on piece variable to a new variable called value, converting it to a float variable
# line 21 prints the value. Observe now that the space is gone

value = float(piece)
print(value)

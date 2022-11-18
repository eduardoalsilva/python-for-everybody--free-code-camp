# Line 3 and line 4 save values 0 to a int variable and 0.0 to a float variable

num = 0
tot = 0.0

# Line 10 to line 19 do a repetition structure that is repeted until the user inputs the word "done"
# The while structure sums all the values the user inputs to a variable, iterates each time the user input any value in another variable


while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
    num = num + 1
    tot = tot + fval

# Line 24 prints the tot variable with all numbers the user typed sumed, the num variable that means how many values (valid or invalid ones) the user entered
# and also inputs the tot variable divided to the num variable.

print(tot,num,tot/num)

# obs.: the programs keeps adding the value saved in fval even if the input is invalid 
# so if the first number you add is 5, and the second one is invalid input, the program will add 5 to the tot variable again.
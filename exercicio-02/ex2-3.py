# Line 6: print a message asking the user to put the amount of worked hours and save it in a variable
# Line 7: print a message asking the user to put the hour rate and save it in a variable
# Line 8: calculates how much the payment is and save it in a variable
# Line 9: print the payment to be done

workedHours = input("Enter Hours: ")
hourRate = input("Enter Rate: ")
payment = float(workedHours) * float(hourRate)
print("Pay: $ ", payment)

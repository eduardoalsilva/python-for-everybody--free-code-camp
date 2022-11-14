## Payment calculator based on worked hours and hour rate

# Line 12 and line 13 save in different variables the amout of worked Hours and the hour rate
# From line 14 to line 18 the program tries save the value if it's a number to a float variable. 
# If it's not a number it prints a error.
# Line 21 prints both worked hours and hour Rate
# From line 22 to line 27 the program tests if the amount of worked hours is higher than 40. 
# If it is higher, it gives 50% more for the overtime, it it's not, it only pays the regular value
# Line 28 prints the final value to be payed


workedHours = input("Enter Hours: ")
hourRate = input("Enter Rate: ")
try:
    floatWorkedHours = float(workedHours)
    floatHourRate = float(hourRate)
except:
    print("Error, please enter numeric input!")
    quit()

print("Amount of worked hours: ",floatWorkedHours, "Hour Rate: ", floatHourRate)
if floatWorkedHours > 40:
    regularPayment = floatHourRate * floatWorkedHours
    overTimePayment = (floatWorkedHours - 40.0) * (floatHourRate * 0.5)
    finalPayment = regularPayment + overTimePayment
else:
    finalPayment = floatWorkedHours * floatHourRate
print("Pay:", finalPayment)
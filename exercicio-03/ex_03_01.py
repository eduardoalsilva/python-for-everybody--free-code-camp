# save in a variable the amount of worked hours wrote by the user
# save in a variable the hours rate wrote by the user
# save the first variable value to a float type variable
# save the second variable value to a float type variable



workedHours = input("Enter Hours: ")
hoursRate = input("Enter Rate: ")
floatWorkedHours = float(workedHours)
floatHoursRate = float(hoursRate)

# tests if the amount of worked hours is higher than 40
# if the sentence is true multiply the amount of worked hours by the hours rate and give 50% more for the overtime
# if the sentence is false, only multiply without extra payment

if floatWorkedHours > 40:
    print("Overtime!!")
    regularPayment = floatWorkedHours * floatHoursRate
    overTimePayment = (floatWorkedHours - 40.0) * (floatHoursRate * 0.5)
    print("Regular payment: $", regularPayment, "\nOvertime payment: $", overTimePayment)
    totalPayment = regularPayment + overTimePayment
else:
    print("Regular")
    totalPayment = floatHoursRate * floatWorkedHours

# print the final amount to be payed
print("Pay: $", totalPayment)

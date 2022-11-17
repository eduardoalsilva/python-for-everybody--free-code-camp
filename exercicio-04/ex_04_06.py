# line 5 to line 14 defines the function computepay with the parameters workedHours and hourRate.
# the function calculates the final payment to be done to the employee. If he worked more than 40 hours, there will be an overtime payment
# it adds 50% for overtime hour.

def computepay(workedHours, hourRate):

    if workedHours > 40:
        regularPayment = workedHours * hourRate
        overTimePayment = (workedHours - 40.0) * (hourRate * 0.5)
        finalPayment = regularPayment + overTimePayment
    else:
        finalPayment = workedHours * hourRate

    return finalPayment

# line 19 and line 20 declares 2 variables
# line 21 and line 22 converts these variables in float, creating 2 new variables

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
floatHours = float(hours)
floatRate = float(rate)

# line 27 runs the function computepay giving the float variables as parameters and save the return to the payment variable
# line 28 prints in the screen the final payment.

payment = computepay(floatHours,floatRate)
print("Pay:", payment)

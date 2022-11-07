def computepay(hours, rate):

    if hours > 40:
        reg = rate * hours
        otp = (hours - 40.0) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = hours * rate

    return pay
sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)
#print(fh, fr)
computepay(fh,fr)

xp = computepay(fh,fr)
print("Pay:", xp)

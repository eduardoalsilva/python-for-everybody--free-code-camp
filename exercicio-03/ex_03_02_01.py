## This program converts the temperature in fahrenheit to celcius

# the line 9 save the value written by the user in a variable called temperature
# the line 10 save the value 0 to the variable called celcius
# the line 11 turn the temperature written by the user in float to a variable called fahrenheit
# the line 12 converts the fahrenheit temperature to celcius
# the line 13 prints it in the screen

temperature = input('Enter the temperature in fahrenheit: ')
celcius = 0
fahrenheit = float(temperature)
celcius = (fahrenheit - 32.0) * 5.0 / 9.0
print("The temperature in celcius is %.2f"% celcius, "celcius degrees")
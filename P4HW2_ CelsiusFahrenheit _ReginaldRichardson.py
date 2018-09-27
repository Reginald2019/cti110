# Program converts Celsius temperature into Farenheit temperature.
# 09/26/18
# CTI-110 P4HW2 - Celsius to Fahrenheit Table
# Reginald Richardson

# Celsius to Fahrenheit
print("Celsius temperature\t to Fahrenheit Equivalent")
print ("---------------------------------------")
for celsius_temp in range (0, 21):
    fahrenheit_temp = 9/5 * celsius_temp + 32
    # Display results
    print(celsius_temp, '\t', fahrenheit_temp)

#_____________________Psuedocode
# Input Title ( optional line break)
# 'for' loop
# Print results

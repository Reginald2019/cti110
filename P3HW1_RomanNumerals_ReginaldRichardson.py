# Program for displaying Roman Numerals. (1 through 10)
# CTI_110
# P3HW1_Roman Numerals
# Reginald Richardson
# September 17, 2018

# Ask for an integer in-between 1 to 10.
integer = int(input('Enter an integer within the range of 1 to 10: '))
    
#If value parameters.
if integer == 1:
    print('The Roman Numeral for 1 is: I')
elif integer == 2:
    print('The Roman Numeral for 2 is: II')
elif integer == 3:
    print('The Roman Numeral for 3 is: III')
elif integer == 4:
    print('The Roman Numeral for 4 is: IV')
elif integer == 5:
    print('The Roman Numeral for 5 is: V')
elif integer == 6:
    print('The Roman Numeral for 6 is: VI')
elif integer == 7:
    print('The Roman Numeral for 7 is: VII')
elif integer == 8:
    print('The Roman Numeral for 8 is: VIII')
elif integer == 9:
    print('The Roman Numeral for 9 is: IX')
elif integer == 10:
    print('The Roman Numeral for 10 is: X')
#If numerical value exceeds ten.
else:
    print('Invalid Entry: Numerical value exceeds specified range')

#_____________________________________________________________________________________________________________________________________Psuedocode
# Prompt user to enter an integer for the numbers 1 through 10
# integer = input "Enter a number within a range of 1 through 10:"
# Set Parameters 
# elif 1 is pressed Print "The Roman Numeral 1 is: I"
# elif 2 is pressed Print "The Roman Numeral 2 is: II"
# elif 3 is pressed Print "The Roman Numeral 3 is: III"
# elif 4 is pressed Print "The Roman Numeral 4 is: IV"
# elif 5 is pressed Print "The Roman Numeral 5 is: V"
# elif 6 is pressed Print "The Roman Numeral 6 is: VI"
# elif 7 is pressed Print "The Roman Numeral 7 is: VII"
# elif 8 is pressed Print "The Roman Numeral 8 is: VIII"
# elif 9 is pressed Print "The Roman Numeral 9 is: IX"
# elif 10 is pressed Print "The Roman Numeral 10 is: X"
#   Print "Invalid Entry: Numerical Value exceeds specified range"

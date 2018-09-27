# Calculate shhipping charges based on weight.
# CTI_110 
# P3HW2_Shipping Charges 
# Reginald Richardson  
# September 19, 2018
#

print('\nWelcome to Fast Freight Shipping ')
#Enter the weight of the package.
weight = float(input('Enter the weight of the package you are shipping in pounds: '))

#Calculate the shipping rate per pound for each set parameter.
shipping_charge_1 = 1.50 * weight
shipping_charge_2 = 3.00 * weight
shipping_charge_3 = 4.00 * weight
shipping_charge_4 = 4.75 * weight

# When to indicate error. 
if weight ==0:
    print('Invalid Entry: package must weighs over 0 pounds.')
    
#2 pounds or less
elif 0 < weight < 3:
    print('The cost of shipping for this package is: $', format(shipping_charge_1, ',.2f'))
    
#Over 2 pounds but not more than 6 pounds
elif 2 < weight < 7:
    print('The cost of shipping for this package is: $', format(shipping_charge_2, ',.2f'))
    
#Over 6 pounds but not more than 10 pounds
elif 6 < weight < 11:
    print('The cost of shipping for this package is: $', format(shipping_charge_3, ',.2f'))
    
#Over 10 pounds
else:
    print('The cost of shipping for this package is: $', format(shipping_charge_4, ',.2f'))
    
#Present error message if package is less than 0 as well
if weight < 0:
    print('Invalid Entry: package must weighs over 0 pounds.')

#________________________________________________________________________________________________________________________________Psuedocode
# Print "Welcome to Fast Freight Shipping" (if needed, add line break)
# Prompt user to enter a weight of a package in pounds
# Enter weight
# Calculate the shipping rate per pound for each set parameter.
# Get the rate per pound for shipping_charge1 through shipping_charge4
# If the input weight = 0 display error
#
# Else-if (elif) weight is 2 pounds or less:
# Else-if (elif) weight is over 2 pounds but not more than 6 pounds:
# Else-if (elif) weight is over 6 pounds but not more than 10 pounds:
# Else if (elif) weight is over 10 pounds:
# Present error message if package is less than 0 as well

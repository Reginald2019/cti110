# This program calculates monthly budgets 
# 09/26/18
# CTI-110 P4HW1 - Budget Analysis
# Reginald Richardson

# Prompt user to enter monthly budget
budget = float(input('Enter current monthly budget: '))
    
# Create variable to control the loop.
keep_going = 'y'
total = 0

# Calculate monthly expenses
while keep_going == 'y':

    # Expense
    expense =float(input('Enter an expense:'))

    # Total expense
    total += expense

    # Additional expense
    keep_going = input('Do you want to enter another' + \
                       'expense (Press y for yes, any other key for no): ')
print()
# Display Budget results
if total >= budget:
    print("You were over your budget of", "$" + format(budget, ",.2f"), \
          "by", "$" + format( total - budget, ",.2f"))
        
elif total <= budget:
        print ("You were under your budget of", "$" + format(budget, ",.2f"), \
               "by", "$" + format(budget - total, ",.2f"))
else:
    print("You used exactly your budget of", \
          "$" + format(budget , ",.2f"),".")
        
        

#_____________________________________________Psuedocode
# Prompt user for budget cost
# Create loop parameters
# Calculate monthly expenses
# Display results
               


 





                   

                   



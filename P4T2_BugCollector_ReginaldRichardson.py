# A brief description of the project
# 09/26/18
# CTI-110 P4T2 - Bug Collector
# Reginald Richardson 
#

# Intialize the accumulator
total = 0

# Get the bugs collected for each day.
for day in range(1, 80):
    # Prompt the user.
    print('Enter the bugs collected on day', day)

    # Input the number of bugs.
    bugs = int(input())

    # Add bugs to total.
    total += bugs

# Display the total bugs.
print('You collected a total of', total, 'bugs. ')

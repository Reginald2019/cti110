# Estimated increase in semester tuition in 5 years.
# 09/26/18
# CTI-110 P4HW3 - Tuition Increase
# Reginald Richardson

# Set tuition amount
tuition = 8000
print('Projected semester tuition in the next 5 years')
# 'for' loop parameters
for year in range (1,6):
    # tuition rate for 5 years
    rate = .03
    tuition = 8000
    # Total
    total =((tuition * rate) * year ) + tuition
    # Display results
    print('The projected semester tuition for year', year, 'is $', total)

#__________________________________Psuedocode
# Enter given tuition amoount
# 'for' loop (controls)
# tuition rate
# total calculations
# results

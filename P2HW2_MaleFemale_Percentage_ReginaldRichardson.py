# Calculating male and female class percentages
# 09/10/18
# CTI-110 P2HW2 - Male Female Percentage
# Reginald Richardson

# Male and female percentage formula.
Male_value = float(input('Enter the number of males in the class'))
Female_value = float(input('Enter the number of females in the class'))
TotalStudent_value = Male_value + Female_value

# Male/Female students divided by total number of students.
MaleStudent_Percentage = Male_value / TotalStudent_value * 100
FemaleStudent_Percentage = Female_value / TotalStudent_value *100

# Male/Female percentage result.
print('There are' + str( TotalStudent_value ) + ' students in the class ' + \
      format( MaleStudent_Percentage, ".0%" ) + ' of them are males and ' + \
      format( FemaleStudent_Percentage, ".0%" ) + ' of them are females')

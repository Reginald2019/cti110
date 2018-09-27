# Converting Number grades into Letter grades.
# CTI_110
# P3Lab_Debugging
# Reginald Richardson
# September 17, 2018
  
# Start-Up of program
print('Grade Changer')
print("About: Convert the numerical value of your grade into a letter value")
print('--------------------------------------------------------------------')

# Prompt user to input numerical value grade.
Test_score = float(input('Enter grade: '))

# Specified grading range.
A_grade = 90
B_grade = 80
C_grade = 70
D_grade = 60

#Determine the grade
if Test_score >= A_grade:
    print('Your current grade is an: A') 
else:
    if Test_score >= B_grade:
        print('Your current grade is an: B')
    else:
        if Test_score >= C_grade:
            print('Your current grade is an: C')
        else:
            if Test_score >= D_grade:
                print('Your current grade is an: D')
            else:
                print('Your current grade is: F')

#_____________________________________________________________________Psuedocode
#Program Start-Up
#User entry of grade
#Grade parameters
#Determine grade 
                

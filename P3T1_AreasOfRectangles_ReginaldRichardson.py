# Calculating area of rectangles program.
# P3HW1 - Roman Numerals 
# Reginald Richardson
# 09/17/18

# Dimensions of rectangle 1.
Length1 = int(input('Enter the length of rectangle 1: '))
Width1 = int(input('Enter the width of rectangle 1: '))

# Dimensions of rectangle 2.
Length2 = int(input('Enter the length of rectangle 2: '))
Width2 = int(input('Enter the length of rectangle 2: '))

# Calculate the areas of the rectangles.
area1 = Length1 * Width1
area2 = Length2 * Width2

#Determine which has the greater area.
if area1 > area2:
    print('Rectangle 1 has the greater area.')
elif area2 > area1:
    print('Rectangle 2 has the greater area.')
else:
    print('Both rectangles have the same area.')

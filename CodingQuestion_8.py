"""
CODING QUESTIONS:7
Write a Python program to convert temperatures to and from celsius, Fahrenheit.
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in
Fahrenheit ]
Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius
"""
temp = input("Enter the temperature in proper format : 120C,67F etc")

degree=int(temp[:-1])
i_convention=temp[-1]

if i_convention.upper()=='C':
    result = int(round(9*degree)/5+32)
    o_convention='Fahreheit'

elif i_convention.upper()=='F':
    result = int(round((degree-32)*5/9))
    o_convention = 'Celsius'

else:
    print('Invalid input format')
    quit()

print(temp,' is ', result,' in ',o_convention )


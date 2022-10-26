#Name: Marcela Soriano Cornejo
#Email: marcela.sorianocornejo40@myhunter.cuny.edu
#Date: September 23, 2022
#This program converts between cm and ft/in

from re import A

print("(a) convert centimeters to feet")
print("(b) convert centimeters to feet and inches")
print("(c) convert feet and inches to centimeters")

choice=input('Enter a or b or c: ')

if choice=='a':
    cm=float(input('Enter height in centimeters: '))
    print('height is',round(cm/30.48,2),'feet')

if choice=='b':
    cm=float(input('Enter height in centimeters: '))
    ft=int(cm/30.48)
    inches = int(((cm - (ft * 30.48)) / 2.54))
    if inches!=0:
        print("height is",ft,'feet and',inches,'inches')
    else:
        print("height is",ft,'feet')

if choice=='c':
    feet_str, inches_str = input("Enter height in feet and inches, separated by a space: ").split()
    feet = int(feet_str)
    inches = int(inches_str)
    centimeters = (feet*30.48)+(inches*2.54)
    print("height is",round(centimeters,1),"cm")

else:
    print("Wrong choice, please enter only a or b or c.")
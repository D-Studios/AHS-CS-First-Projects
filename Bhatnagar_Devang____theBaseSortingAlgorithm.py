import sys

base=int(input("Give a base "))
decimalNumber=int(input("Give a decimal number "))
digits=[]
division=decimalNumber
while division>0:
    letters=False
    letter=''
    division=int(decimalNumber/base)
    carry=decimalNumber%base
    if carry>9:
        letters=True
    if carry==10:
        letter='A'
    elif carry==11:
        letter='B'
    elif carry==12:
        letter='C'
    elif carry==13:
        letter=='D'
    elif carry==14:
        letter='E'
    elif carry==15:
        letter='F'
    if letters==False:
        digits.append(str(carry))
    else:
        digits.append(letter)
    decimalNumber=division

string=""
for x in reversed(range(len(digits))):
    string+=digits[x]
print(string)

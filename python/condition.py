age = 70 #nested if-else Statement
is_member=True
if age >= 60:
    if is_member:
        print("30% senior Discount!")
    else:
        print("20% senior Discount!")
else: 
    print("Not eligible for a senior discount.")    
# Conditional Expression
Age = 21
s="Adult" if age >= 18 else "Minor"
print(s)
# Match-case Statement
number = 2
match number:
    case 1:
        print("Tow")
    case 2:
        print("Two or Three")
    case 3:
        print("Other number")
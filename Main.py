Num = []
Count = int(input("How Many Number You Want to Enter : "))
for i in range(0,Count):
    User_Indexes = int(input("Enter the Number : "))
    Num.append(User_Indexes)
Num.sort()
print(f"The Second Largest Number is :- {Num[1]}")

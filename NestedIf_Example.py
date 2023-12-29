salary=int(input("Salary:"))
age=int(input("Age:"))
if (salary>=2000 and age>=20):
    loan=int(input("Loan:"))
    if(loan>30000):
        print("Max loan is 20000")
    else:
        print("Eligible for loan")
else:
    print("Not Eligible")
    


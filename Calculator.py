# Asking to user for Operation
print("'1' for Addition")
print("'2' for Subtration" )
print("'3' for Multiplication")
print("'4' for Division")
operation=int(input("write: "))

# Asking number to User
n1=float(input('Enter the First Number: '))
n2=float(input('Enter the Second Number: '))

#Making calculation and printing the answer according to choice of operation.
if operation==1:
    print(n1,'+',n2,'=',n1+n2)
elif operation==2:
    print(n1,'-',n2,'=',n1-n2)
elif operation==3:
    print(n1,'×',n2,'=',n1*n2)
elif operation==4:
    print(n1,'÷',n2,'=',n1/n2)
else:
    print("can't performed.")
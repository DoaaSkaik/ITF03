number=int(input("Enter number to find factorial : "))
if number==0 or number==1 :
    factorial=1
    print("the factorial of " ,number, "=",factorial)
elif number<0:
    print("Sorry the number doesnt have a factorial !")
elif number>1:
    factorial=1
    for i in range(1,number+1) :
        factorial=factorial*i
    print("the factorial of " ,number,"=",factorial)
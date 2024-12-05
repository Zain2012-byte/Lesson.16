def factorial(x):
    '''This is a recursive functionto find the factorial of an integer'''
    if x==0 or x==1:
        return 1
    else:
        #calling function insode a funtion
        return x*factorial(x-1)

        #5! = 5 * 4 * 3 * 2 * 1

print(factorial.__doc__)
print("the factorial of 0:",factorial(0))
print("the factorial of 1:",factorial(1))
print("the factorial of 2:",factorial(2))
print("the factorial of 7:",factorial(7))
print("the factorial of 9:",factorial(9))
print("the factorial of 10:",factorial(10))




    

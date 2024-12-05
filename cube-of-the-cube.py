def cube(number):
    return number*number*number

#define a funtion which will execute cube function if the user entered number is dividible by 3

def by_three(number):
    if number%3 == 0:
        return cube(number)
    else:
        return False 

print(by_three(9))
print( by_three(4))
#Calculate Factorial Using a Function

i = int(input('Enter a number: '))

def factorial(i):
    if i < 2:
        return 1
    else:
        return i * (factorial(i-1))
    

result = factorial(i)

print('Factorial of',i,'is: ',result)

#the last two digits of fibanoski 
n=int(input("write the number")) 
def nth_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)

x=nth_fibonacci(n - 1) + nth_fibonacci(n - 2)
y=x%100
print(y)

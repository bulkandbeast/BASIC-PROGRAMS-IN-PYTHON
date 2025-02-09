#nth fibbanoski number
#the sum of the(n-1)+(n-2)=n
n=int(input("write the number")) 
def nth_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)

print("nth Fibonacci Number:", nth_fibonacci(n))

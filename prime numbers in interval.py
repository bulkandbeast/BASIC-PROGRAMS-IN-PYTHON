#all prime numbers in an interval
a=int(input("enter the first number"))
b=int(input("enter the second number"))
def primes_in_interval(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
    return primes

print("Prime numbers between the given intervals are:", primes_in_interval(a,b))

principal=int(input("write the principal amount"))
rate=int(input("what is the rate of intrest"))
time=int(input("what is the time period"))
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

print("Simple Interest for the amount", simple_interest(principal,rate,time))

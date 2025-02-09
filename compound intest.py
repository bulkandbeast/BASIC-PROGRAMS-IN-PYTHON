#compound intrest
principal=int(input("write the principal amount"))
rate=int(input("what is the rate of intrest"))
time=int(input("what is the time period"))
def compound_interest(principal, rate, time):
    return principal * ((1 + rate / 100) ** time) - principal

print("Compound Interest for the given values are:", compound_interest(principal,rate,time))

#checking whether armstrong
num=int(input("enter the number"))
def is_armstrong_number(num):
    digits = list(map(int, str(num)))
    return num == sum([d**len(digits) for d in digits])
print("Is the given value an Armstrong Number?", is_armstrong_number(num))

num = int(input("Please enter the number you want to find the power of: "))
power = int(input("In what, power do you want to find out the number's power: "))

result = 1

for i in range(power):
    result *= num

print("Result: ", result)
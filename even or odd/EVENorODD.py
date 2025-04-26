import sys
print("Welcome to EvenORodd")
try:
    num = int(input("which is the number you want to check?\n"))
except:
    print("A decimal number cannot be defined as even or odd.")
    sys.exit()

if num % 2 != 0:
    print(f"{num} is a odd number")
else:
    print(f"{num} is a even number")

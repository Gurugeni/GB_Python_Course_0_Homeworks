# Задача 1


num = int(input("Choose your destiny!Enter number 0_-: "))
while num > 0:
    print(num%10)
    num //= 10
print("That's your destiny! Don't ask me what is it. Be conqueror or die!")


# Задача 2

a = int(input("Input First Number: "))
b = int(input("Input Second Number: "))
a, b = b, a

# Задача 3

age = int(input("Input age: "))

if age >= 18:
    print("Yes")
else:
    print("No")
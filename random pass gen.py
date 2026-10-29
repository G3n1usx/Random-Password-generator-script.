import random
import secrets

alphabet = [
  "A", "B", "C", "D", "E", "F", "G",
  "H", "I", "J", "K", "L", "M", "N",
  "O", "P", "Q", "R", "S", "T", "U",
  "V", "W", "X", "Y", "Z"
]

numerics = [1,2,3,4,5,6,7,8,9,10]

password = " "
for i in range(5):
    alpha1 = random.randint(0,25)
    num1 = random.randint(0,9)
    num2 = str(numerics[num1])
    password += num2
    password += alphabet[alpha1]


print("Your password is " + password)
x = input("Do you want to reroll your password: ")

if x.lower() == "yes":
    password = " "
for i in range(5):
    alpha1 = random.randint(0,25)
    num1 = random.randint(0,9)
    num2 = str(numerics[num1])
    password += num2
    password += alphabet[alpha1]


print("Your password is " + password)

y = input("Press enter to exit... ")
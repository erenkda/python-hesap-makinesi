num1 = int(input("Lütfen birinci sayıyı belirtiniz: "))
num2 = int(input("Lütfen ikinci sayıyı belirt: "))

op = input("Bir işlem seçiniz. (+, -, *, /): ")

if op == "+":
    print(num1, "+", num2, "=", num1+num2)
elif op == "-":
    print(num1, "-", num2, "=", num1-num2)
elif op == "*":
    print(num1, "x", num2, "=", num1*num2)
elif op == "/":
    print(num1, "/", num2, "=", num1/num2)
else:
    print("Lütfen geçerli bir işlem belirt.")

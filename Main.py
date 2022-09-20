print("hellow\n")
print("input two number and mathematic opperationor it")
x1 = float(input())
operation = input()
x2 = float(input())
if operation == "+":
    print(x1 + x2)
elif operation == "-":
    print(x1 - x2)
elif operation == "*":
    print(x1 * x2)
elif operation == "/":
    if x2 == 0:
        print("error")
    else:
        print(x1 / x2)

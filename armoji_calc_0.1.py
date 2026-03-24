x = int(input("x: "))
y = int(input("y: "))
ifz = input("z?(y/n): ")

if ifz == "y":
    z = int(input("z: "))

    funz = input("add, mul, div, sub: ")

    if funz == "add":
        print(x + y + z)
    elif funz == "mul":
        print(x * y * z)
    elif funz == "div":
        print(x / y / z)
    elif funz == "sub":
        print(x - y - z)
    else:
        print("error")

elif ifz == "n":
    fun = input("add, mul, div, sub: ")

    if fun == "add":
        print(x + y)
    elif fun == "mul":
        print(x * y)
    elif fun == "div":
        print(x / y)
    elif fun == "sub":
        print(x - y)
    else:
        print("error")

else:
    print("error")



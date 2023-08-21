a = int(input("Enter a:"))
b = int(input("Enter b:"))


def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)


print(mcd(a, b))

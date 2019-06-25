a = float(input("nhập a: "))
b = float(input("nhập b: "))
c = float(input("nhập c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("PT vô số nghiệm!")
        else:
            print("PT vô nghiệm!")
    else:
        if c == 0:
            print("PT có 1 nghiệm x = 0")
        else:
            print("PT có 1 nghiệm x = ", -c / b)
else:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("nghiệm phức x1 = ", (-b + complex(delta**0,5))/2*a)
        print("nghiệm phức x2 = ", (-b - complex(delta ** 0,5))/2*a)
    elif delta == 0:
        print("PT có nghiệm duy nhất: ", -b /(2*a))
    elif delta>0:
        print("nghiệm x1= ", (-b + delta ** 0,5) / 2*a)
        print("nghiệm x2= ", (-b - delta ** 0,5) / 2*a)
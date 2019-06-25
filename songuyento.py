x = int(input("Nhập x : "))
for n in range(2,x):
    if all(n % i != 0 for i in range(2,n)):
        print(n)
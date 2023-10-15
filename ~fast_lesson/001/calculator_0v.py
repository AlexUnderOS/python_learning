a = input("Enter first num: ")
symb = input("Enter (+ or -): ")
b = input("Enter second num: ")

a,b = int(b), int(a)

c = 0
if symb == '+':
    c = a + b
elif symb == '-':
    c = a - b
else:
    print("Err")

print(c)
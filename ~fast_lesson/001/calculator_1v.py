import colorama as col
from colorama import init
init()


a = input(f"{col.Fore.GREEN}Enter first num: ")
symb = input(f"{col.Fore.RED}Enter (+ or -): ")
b = input(f"{col.Fore.GREEN}Enter second num: ")

a,b = int(b), int(a)

c = 0
if symb == '+':
    c = a + b
elif symb == '-':
    c = a - b
else:
    print("Err")

print(col.Back.WHITE,c)
print(col.Back.RESET)

input()
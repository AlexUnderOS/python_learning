a,b = 5,10

c = a + b
print("+",c)

c = a / 2
print("/",c)

c = a // 2
print("//",c)

c = b % 3
print("%",c)

c = a ** 2
print("**",c)


print()
#priority
c = 3 + 4 * 5 ** 2 + 7
print("1. **\n2. *\n3. +")
print("answer1 =",c)

c = (3 + 4) * 5 ** 2 + 7
print("answer2 =",c)


print()
#unary minus

d = 10
unary = -d #change to -
print(unary) 

d = -10
unary = -d #change to +
print(unary) 


print()
#round
print(round(4.5))



print("\n\t***MATH***")
#math
import math
print(math.floor(5.9))
print(math.ceil(5.1)) #!= round
print(math.pi)
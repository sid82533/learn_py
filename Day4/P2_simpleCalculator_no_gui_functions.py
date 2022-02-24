def add(a,b):
    print(int(a) + int(b))

def difference(a,b):
    print(int(a) - int(b))

def product(a,b):
    print(int(a) * int(b))

def division(a,b):
    print(int(a) / int(b))

a = input("First Number: ")
b = input("Second Number: ")
c = input("Operation(+, -, *, /): ")

if c == '+':
    add(a,b)
elif c == '-':
    difference(a,b)
elif c == '*':
    product(a,b)
else:
    division(a,b)
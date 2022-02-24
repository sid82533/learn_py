a = input("First Number: ")
b = input("Second Number: ")
c = input("What would you like to perform (+, -, *, /): ")

if c == '+':
    print(int(a) + int(b))
elif c == '-':
    print(int(a) - int (b))
elif c == '*':
    print(int(a) * int (b))
else:
    print(int(a)/int (b))

# print(addition)
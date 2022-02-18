# Python strings are immutable
# chracters can be accessed using [] - 0 based indexing

s = "hello"
print(s[2])

# len - displays the length of the string

print(len(s))

# + operator can concatenate only 2 strings. If there is any other variable that is not string - convert using str()

print("This is a string - "+s)

pi = 3.14
print("The value of pi is - " + str(pi))

not_raw = 'this\t\n and that'
print(not_raw)
raw = r'this\t\n and  that' # prefix r before a string that has new line and new tab characters, 
                            #prevents from the applocation of those characters. 
print(raw)

multi = """It was the best of times. 
It was the awesomest of times."""
print(multi)
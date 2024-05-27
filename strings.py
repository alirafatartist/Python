# teiple qoutes output new line
mystr1 ="""first
second
third
"""
print(mystr1)
    # first
    # second
    # third 

mystr2 ='''first
second
third
'''
print(mystr2)
    # first
    # second
    # third 


# and escape
mystr3 ='''first
second "forth" 'test'
third
'''
print(mystr3)
    # first
    # second "forth" 'test'
    # third

# Slicing
# indexing
mystring = "Free Palestine"
print(mystring[0]) #F
print(mystring[-1]) #e
print(mystring[5]) #P
print(mystring[-9]) #P

# Slicing ( Access Multiple Sequence Items )
# [Start:End] End Not Included
# [Start:End:Steps]

print(mystring[0:4]) #Free
print(mystring[-9:]) #Palestine
print(mystring[:4]) #Free
print(mystring[0:]) #Free Palestine
print(mystring[:]) #Free Palestine
print(mystring[::1]) #Free Palestine
print(mystring[::2]) #Fe aetn

# ways to print es
print(mystring[8:10]) #es
print(mystring[-6:-4]) #es
print(mystring[-6:-4:1]) #es

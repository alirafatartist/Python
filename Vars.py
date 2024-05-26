# Rules of writing variables

myvar = "string"
print(myvar)
# string

_myvar = "string"
print(_myvar)
# string


# not allowed to write vars start with numbers or special characters @ - $ ! 
100myvar = "string"
print(100myvar)
# SyntaxError: invalid decimal literal

@myvar = "string"
print(@myvar)
# SyntaxError: invalid syntax

# Note: you can put numbers in middle of var but you can't put special characters in middle
my100var = "string"
print(my100var)
# string

my-var = "string"
print(my-var)
# SyntaxError: invalid syntax

name = "alirafatartist"  # Single Word => Normal
myName = "alirafatartist"  # Two Words => camelCase
my_name = "alirafatartist"  # Two Words => snake_case




# Part #2

# Reserved Words
help("keywords")
"""
Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from
or
None                continue            global
pass
True                def                 if
raise
and                 del                 import
return
as                  elif                in
try
assert              else                is
while
async               except              lambda
with
await               finally             nonlocal
yield
break               for                 not
"""

a, b, c = 1, 2, 3

print(a)
print(b)
print(c)
# 1
# 2
# 3

e, f, g = 1, 2,
print(e)
print(f)
print(g)
# ValueError: not enough values to unpack (expected 3, got 2) 

k, h, i = 1, 2, 7, 8

print(k)
print(h)
print(i)
# ValueError: too many values to unpack (expected 3) 

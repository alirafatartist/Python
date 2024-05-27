# ---------------------
# -- Strings Methods --
# len(str) >> calc string length
# str.strip() >> remove spaces from right and left
# str.lstrip() >> remove spaces from left
# str.rstrip() >> remove spaces from right
# str.strip(what do you need to remove) >> remove what do you need
# str.title() >> used to convert the first character of each word in a string to uppercase and all other characters to lowercase
# str.upper() >> make all characters uppercase
# str.lower() >> make all characters lowercase
# str.capitalize() >> make first character of the string capital
# str.zfill() >> used to pad a numeric string on the left with zeros
# ---------------------

a = "Free Palestine"
b="      Free Palestine      "
c="@$Free Palestine@$"
m="i love 2d Graphics and 3g Technology and python"
f,j="111","1"
print(len(a)) #14
print(len(b)) #26
print(b.strip()) #Free Palestine
print(b.lstrip()) #'Free Palestine      '
print(b.rstrip()) #      Free Palestine
print(c.strip("@$")) #Free Palestine
print(m.title()) # I Love 2D Graphics And 3G Technology And Python
print(m.upper()) # I LOVE 2D GRAPHICS AND 3G TECHNOLOGY AND PYTHON
print(m.lower()) # i love 2d graphics and 3g technology and python
print(m.capitalize()) # I love 2d graphics and 3g technology and python
print(f.zfill(4)) # 0111
print(j.zfill(4)) # 0001

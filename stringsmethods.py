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
# str.split(split character,how many items i want to split) >> gives a list of string depend on split character
# str.rsplit(split character,how many items i want to split) >> gives a list of string depend on split character but from right
# str.center(,character)used to center-align a string within a specified width. It pads the string with a specified character (default is space) on both sides, if necessary, to make sure the total width of the string is equal to the specified width.
# str.count(word i want to count in string, strat index, end index)
# str.swapcase() >> swape each character case (small 🔄 capital)
# str.startswith("word") check if string starts with this word
# str.endswith("word") check if string ends with this word
# str.index("character",start index, end index) >> find the index of the character and when the character not found it's throuht error
# str.find("character",start index, end index) >> find the index of the character and when the character not found it's throuht -1
# str.rjust(width,fill character) >> from right
# str.ljust(width,fill character) >> form left
# ---------------------

a = "Free Palestine"
b="      Free Palestine      "
c="@$Free Palestine@$"
m="i love 2d Graphics and 3g Technology and python"
f,j="111","1"
countries = "egypt,libya,qater"
p= "I-Love-Python-and-PHP-and-MySQL"
e = """First Line
Second Line
Third Line"""
k="First Line\nSecond Line\nThird Line"
g = "Hello\tWorld\tI\tLove\tPython"
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
print(a.split()) # ['Free', 'Palestine']
print(countries.split(",")) # ['egypt', 'libya', 'qater']
print(countries.split(",",1)) # ['egypt', 'libya,qater']
print(p.split("-",3)) # ['I', 'Love', 'Python', 'and-PHP-and-MySQL']
print(p.rsplit("-",3)) # ['I-Love-Python-and', 'PHP', 'and', 'MySQL']
print(f.center(10)) #    111    
print(f.center(10,"#")) # ###111####
print(p.count("and")) # 2
print(p.count("and",0,18)) # 1
print(a.swapcase()) # fREE pALESTINE
print(countries.startswith("egypt")) # true
print(countries.endswith("sudi")) # false
print(a.index("P")) # 5
# print(a.index("P",0,4)) # ValueError: substring not found
print(a.find("P",0,4)) # -1
print(f.rjust(6,"k")) # kkk111
print(f.ljust(6,"k")) # 111kkk
print(e.splitlines()) # ['First Line', 'Second Line', 'Third Line']
print(k.splitlines()) # ['First Line', 'Second Line', 'Third Line']
print(g.expandtabs(10)) # Hello     World     I         Love      Python


seven = "osama_elzero"
eight = "OsamaElzero100"
nine = "Osama--Elzero100"

print(seven.isidentifier())
print(eight.isidentifier())
print(nine.isidentifier())


x = "AaaaaBbbbbb"
y = "AaaaaBbbbbb111"
print(x.isalpha())
print(y.isalpha())

print("abc123".isalnum())        # True: all characters are letters or digits
print("abc123!".isalnum())       # False: contains a special character (!)
print("123".isalnum())           # True: all characters are digits
print("abc".isalnum())           # True: all characters are letters
print("abc 123".isalnum())       # False: contains a space
print("".isalnum())              # False: empty string
print("αβγ123".isalnum())        # True: contains Greek letters and digits
print("αβγ!".isalnum())          # False: contains a special character (!)

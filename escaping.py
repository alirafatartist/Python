# ---------------------------------------------
# Escape Sequences Characters
# \b    => Back Space
# \n    => Newline (Escape New Line + \)
# \\    => Escape Back Slash
# \'    => Escape Single Quotes
# \"    => Escape Double Quotes
# \n    => Line Feed
# \r    => Carriage Return
# \t    => Horizontal Tab
# \xhh  => Character Hex Value
# ---------------------------------------------

# Escape New Line + Back Slash
print("Hello \
I Love \
Python")
    # Hello I Love Python


# Newline and Tab
print("Line1\nLine2\nLine3")
    # Line1
    # Line2
    # Line3


print("Column1\tColumn2\tColumn3")
    # Column1 Column2 Column3


# Including quotes
print('She said, "Hello!"')
print("It's a wonderful day")
    # She said, "Hello!"
    # It's a wonderful day


# Escape Single Quote
print('I Love Single Quote \'Test\' ')
    # I Love Single Quote 'Test'


# Escape Double Quotes
print("I Love Double Quotes \"Test\" ")
    # I Love Single Quote "Test"


# Backslashes
print("This is a single backslash: \\")
print("File path on Windows: C:\\Users\\Name")
    # This is a single backslash: \
    # File path on Windows: C:\Users\Name


# Carriage return and backspace
print("Hello\rWorld")  # World replaces Hello
print("Hello\bWorld")  # Removes the 'o' in Hello
    # World
    # HellWorld


# Horizontal Tab
print("Hello\tPython")
    # Hello   Python


# Unicode and hexadecimal
print("Heart symbol: \u2764")
print("Letter A in hex: \x41")
    # Heart symbol: ❤
    # Letter A in hex: A


# Octal
print("Letter A in octal: \101")
    # Letter A in octal: A

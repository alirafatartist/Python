# Assigmnet 1
name = "Osama"
age = 38
Country ="Egypt"

print(f"Hello '{name}', How You Doing \\"+ '""" ' + f'Your Age Is "38"" + And Your Country Is: {Country}')
# Hello 'Osama', How You Doing \""" Your Age Is "38"" + And Your Country Is: Egypt

# Assigmnet 2
print(f"Hello '{name}', How You Doing \\" +"\n" '""" ' + f'Your Age Is "38"" +{"\n"}And Your Country Is: {Country}')
# Hello 'Osama', How You Doing \
# """ Your Age Is "38"" +
# And Your Country Is: Egypt

# Assigmnet 3
name = 'Elzero'
print(f"Second Letter Is " + f'"{name[1]}"')
print(f"Third Letter Is " + f'"{name[2]}"')
print(f"Last Letter Is " + f'"{name[3]}"')
# Second Letter Is "l"
# Third Letter Is "z"
# Last Letter Is "e"

# Assigmnet 4
name = 'Elzero'
print(name[1:4]) # lze
print(name[0::2]) # Ezr
print(name[-2::-2]) # rzE

# Assigmnet 5
name = "#@#@Elzero#@#@"
print(name.strip("#@#@")) #Elzero

# Assigmnet 6
num = "9"
print(num.zfill(4)) #0009
num = "15"
print(num.zfill(4)) #0015
num = "130"
print(num.zfill(4)) #0130
num = "950"
print(num.zfill(4)) #0950
num = "1500"
print(num.zfill(4)) #1500

# Assigmnet 7
name_one = "Osama"
name_two = "Osama_Elzero"
print(name_one.rjust(20,"@")) #@@@@@@@@@@@@@@@Osama
print(name_two.rjust(20,"@")) #@@@@@@@@Osama_Elzero

# Assigmnet 8
name_one = "OSamA"
name_two = "osaMA"
print(name_one.swapcase()) # osAMa
print(name_two.swapcase()) # OSAma


# Assigmnet 9
msg = "I Love Python And Although Love Elzero Web School"
print(msg.count("Love")) # 2


# Assigmnet 10
name = 'Elzero'
print(name.index("z")) # 2


# Assigmnet 11
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3","Love",1)) # I Love Python And Although <3 Elzero Web School


# Assigmnet 12
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3","Love")) # I Love Python And Although Love Elzero Web School


# Assigmnet 13
name = "Osama"
age = 38
country = "Egypt"
print(f"My Name IS {name}, And My Agw Is {age}, And My Country Is {country}") #My Name Is Osama, And My Age Is 38, And My Country Is Egypt

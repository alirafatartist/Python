name = input("Please enter your name: ")
age = int(input("How old are you: "))
tall = float(input("How tall are you: "))
weight = float(input("How weight are you: "))
life_equ = ((tall / weight) * age) + 10
birth_year = 2024 - age

print("============")
print(f"Welcome, {name.title()}")
print(f"You will live untill, {(birth_year + life_equ):.0f}, and you will be {life_equ:.0f} years old")

# Please enter your name: maha ahmed
# How old are you: 29
# How tall are you: 163
# How weight are you: 60
# ============
# Welcome, Maha Ahmed
# You will live untill, 2084, and you will be 89 years old

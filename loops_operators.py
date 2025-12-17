fruits = [
    'apple', 
    'orange', 
    'pinapple', 
    'grapes', 
    'banana', 
    'kiwi', 
    'avacado', 
    'lemon', 
    'watremelon'
    ]

for f in fruits:
    print(f)
print("-------------------------------------------------\n")

for f in fruits[2 : 5]:
    print(f)
print("-------------------------------------------------\n")

for f in fruits[: 5]:
    print(f)
print("-------------------------------------------------\n")

for f in fruits[2 : ]:
    print(f)
print("-------------------------------------------------\n")

a   = True
b   = False

print(a and b)
print("-------------------------------------------------\n")
print(a or b)
print("-------------------------------------------------\n")
print(not a)

x = 10 #1010
y = 5  #0101

print(f"x & y : { x & y}") #0000
print(f"x | y : { x | y}") #1111
print(f"x ^ y : { x ^ y}") #1111
print(f"~x : {~x}")        #0101
print(f"y << 2 { y << 2}") #1010
print(f"x >> 2 { x >> 2}") #0101
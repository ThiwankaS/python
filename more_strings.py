'''
here is the algorytmic way of understaind this, btu there is a better way of doing this
'''

print ("Method 01 : "
"-------------------------------------- \n")
# string that need to look upto
str1 = "this has a space in it"
# find the first index where space exists
pos = str1.find(' ')
# untill the str1ing contains a space
while (pos != -1):
    # create a new str1ing until first space
    word = str1[:pos]
    # print it
    print(word)
    # copying the rest of the str1ing 
    str1 = str1[pos + 1:]
    # find the next space
    # if there is no space find will return -1
    pos = str1.find(' ')
# print the last word
print(str1)

print ("Method 02 : "
"-------------------------------------- \n")
# new string need to llok upto
str2 = "this has a space in it"
# 
words = str2.split(' ')
for text in words:
    print(text)
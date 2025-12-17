# the string need to look upto
str = "1234567a"

# my custome function
def isContainDigits(str):
    for c in str:
        if c.isdigit():
            return True
    return False
# check if the string contains at least one digit
if(isContainDigits(str)):
    print("'{}' at least one digit \n".format(str))
else:
    print("'{}' dose not contains any digit \n".format(str))

# check the string is a numeric literal
if(str.isdigit()):
    print("'{}' is a numeric literal \n".format(str))
else:
    print("'{}' is not a numeric literal \n".format(str))
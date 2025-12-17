# expecting user to input a name
name = input("Enter your name : ")

# untill user input is empty this will prompt
while (len(name) == 0):
    print("You are expect to enter your name !")
    print("Enter 'Exit' to exit the program.")
    name = input("Enter your name : ")

# if user input exit then leave the program 
if(name.lower() == "exit"):
    print("ok, exiting the program!")
# is user input aything other than 'Exit' will consider as a valid name
else:
    name = "Mr." + name
    print ("Hello, {}".format(name.capitalize()), end="\n")
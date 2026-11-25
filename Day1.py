name = " Arun G "
work = "Software Dev"
age = 38
weight = 62.5
isMarried = True
Ok = False


print(f"{name.strip()} {age} {weight:.2f}")
print(name.upper())
print(name.replace("G", "GGGG"))
print(len(name))
print(name.strip())
print(name[0:3])
print(age)
print(type(weight))
print(isMarried)
print(Ok)


newName = input("What is your Name")
newAge = int(input("What is your Age"))
print(f"Hi {newName} Your age is {newAge}")


#test
var1 = input("Enter 1st number: ")
var2 = input("Enter 2nd number: ")
var3 = input("Enter Operation like +, -, *: ")
output = int(var1+var2)
print(output)
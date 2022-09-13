# 1st Question

# length of a string
inp = ""
inp2 = "Hello"
inp3 = "Amazing"

print(len(inp3))

#2nd Question

#index of a string.
y = "Pizza"  

num = int(input("Enter index: "))
print(y[num])


s = ""
if len(s) == 0:
    print("Empty String")

z = "World"
num2 = int(input("new number sir!: "))
for i in z:
    if num2 > len(i):
        print("i is out of range")
        break
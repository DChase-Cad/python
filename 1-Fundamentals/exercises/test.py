x = 0
while x < 10:
    print(x)
    x = x+1
    if x == 1:
        print("small")
    if x > 2:
        x = x+1
        print("medium")
    if x == 5:
        x = 7
        print("big")

d=9.0
print(type(d))

my_tuple = (1,2,3,4)
my_set = {1,2,3,4}


print(my_tuple == my_set)

x = 10 
if x < 11 and x > 9: 
    print("if") 
elif x > 10: 
    print("elif") 
else: 
    print("else") 

while True: 
    print("True") 
    break 
    print("Break") 
    break 
    print("False") 

print(1 > 3 or 2 > 1)

x = 1 + (0 * 10) * 3 / 8 ** 1
print(x)
x = 1 + (0 * 10) * 3 // 8 ** 1
print(x)
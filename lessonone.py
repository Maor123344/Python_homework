#print("hello world")

mystring = "hello world"
# print(mystring)

my_list = mystring.split()
# print(type(my_list))

# print(my_list[0][-1])

for char in mystring:
    print(char)
print("-----------")
for str in my_list:
    print(str)
print("------------")
for i in range(len(my_list)):
    print()
    for j in range(len(mystring)):
        print(my_list[i], mystring[j], sep= ",", end="")
        
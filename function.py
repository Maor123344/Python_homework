# def crazy_funk(): 
#     x = "maylindenberg"
#     i = 0  

#     for letter in x: 
#         if i % 2 == 0: 
#             print(letter.lower(), end= "")
#         else:
#             print(letter.upper(), end= "")
#         i += 1  

# crazy_funk()

# import random

# def div(n1, n2):
#     if n2 == 0:
#         return -1
#     return n1 / n2
    

# n1 = random.randint(0, 10)
# n2 = random.randint(0, 10)
# print(f"{n1} / {n2} = {div(n1,n2)}")

# def combine(s1, s2):
#     if len(s1) > len(s2):
#         return s1 + s2
#     return s2 + s1
# s1 = "hello", s2 = "my name is"
# combine(s1,s2) => "my name is hello"
# אורך של מחרוזת בעזרת הפקודה len
# def main():  ## main function
#     name = "omer"
#     text = "my name is "
#     print(combine(name, text))
#     print(combine(text, "jim"))



# def only_even(number):
#     mylist = []
#     for i in range(number):
#         if i % 2 == 0:
#             mylist.append(i)
#     return mylist    
        
# def only_three(given_list):
#     mylist = []
#     for i in given_list:
#         if i % 3 == 0:
#             mylist.append(i)
#     return mylist



# def main():
#     mylist = only_even(100)
#     list1 = [i for i in range(100)]
    
#     x = only_three(list1)
#     print(x)
# main()


def numbers(number):
    list = []
    for i in range (0,number):
        if i %2 and i %3 ==0:
            list.append(i)
    return list

print(numbers(100))

numbers()
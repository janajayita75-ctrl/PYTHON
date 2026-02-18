# f = open("demo.txt","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# f = open("demo.txt","r")
# data = f.read(5)
# print(data)
# f.close()

# f = open("demo.txt","r")
# line1 = f.readline()
# print(line1)
# f.close()

# f = open("demo.txt","w")
# f.write("I want to learn JAVA")
# f.close()

# with open("demo.txt","a") as f:
#     data = f.read()
#     print(data)

# with open("demo.txt","w") as f:
#     f.write("new data")

# import os
# os.remove("demo.txt")

# with open("practie.txt","w")as f :
#     f.write("Hi everyone.\nwe are learning file i/o using java.\nI like programming in Java")


# with open("practie.txt","r")as f :
#   data =  f.read()

# new_data = data.replace("java" , "python")
# print(new_data)

# with open("practice.txt","w") as f:
#    f.write(new_data)

# def check_for_word():
#      word = "learning" 
#      with open("practice.txt","r") as f:
#        data = f.read()
#      if(data.find(word) != -1):
#       print("found")
#      else:
#       print("not found")
# check_for_word()

# ef_checkd_for_line():
#     word = "learning"
#     data = True
#     line no=1
#     with open("practice.txt","r") as f:
#          while data:
#             data = f.readline()
#             if(word in data):
#                print(line no 1)
#                line no+=1

# with open("practice.txt","r") as f:
#    data = f.read()
#    print(data)
# marks = [3,5,6]
# print(marks[1:-1])
# print(marks[1:4:2])
# print(len(marks))
# list = [i for i in range(4)]list comprehension
# print(list)
# list =[1,2,3,4]
# list.append(9)
# list.sort(reverse=True)
# list.reverse()
# print(list.index(1))
# print(list.count(1))
# m= list.copy()
# m[0]=0
# print(list)
# list.insert(1.0)
# m = [89,90,76]
# list.extend(m)
# k = list+m
# print(k)
# tup = (1,5,6)
# print(type(tup),tup)
# print(tup[-1])
# tuple1=(1,2,3,4,5,6)
# res=tuple1.index(5,7,9)
# res=tuple1.count(3)
# res=tuple1.index(3)
# print("count of 3 in tuple1 is:",res)
# import time
# t = time.strftime("%H:%M:%S")
# hour = int(time.strftime("%H"))
# print(hour)

# if(hour>0 and hour<12):
#     print("Good morning sir!")
# elif(hour>12 and hour<17):
#       print("Good Afternoon stir!")
# elif(hour>0 and hour<12):
#      print("good morning sir!")
# letter = "hey my name is harry {} and i am from{} "
# country = "india"
# name = "harry"

# print(letter.format(country,name))
# print(f"hey my name is{name} and i am from {country}")

# price = 89.900
# txt = f"for only{price:.2f} dollars!"
# print(txt)
# print(txt.format())
# def square(n):
#     print(n**2)
# square(5)
# print(square.__doc__)
# def factorial(n):
#     if(n==0 or n==1):
#         return 1 
#     else:
#         return n*factorial(n-1)
# print(factorial(6))

# def fibonacci(n):
#     if(n==0):
#         return 0
#     elif(n==1):
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# print(fibonacci(8))
# s={1,2,3,4,5}
# s1={1,2,5,6}
# s2={1,2,3}
# print(s1.union(s2))
# s1.update(s2)
# print(s1,s2)
# s1.intersection_update(s2)
# print(s)
# dict = {
# "harry":"human being",
# "spoon":"object"
# }
# print(dict)

# ep1 = {122:45,123:56,124:67}
# ep2 = {222:67,566:78}
# ep1.update(ep2)
# print(ep1)
# ep1.clear()
# ep1.pop(122)
# print(ep1)

# for i in range(7):
#     print (i)
#     if i ==5:
#         break

# else:
#     print("sorry no i")

# i = 0
# while i<7:
#     print (i)
#     i = i+1
#     # if i ==4:
#     #     break

# else:
#     print("sorry no i")

# a = input("Enter the number:  ")
# print(f"Multiplication table of {a} is: ")

# for i in range(1,11):
#     print(f"{int(a)}x{i}={int(a)*{i}}")

a = 330
b = 3303
print("A") if a>b else print("=") if a == b else print("B")



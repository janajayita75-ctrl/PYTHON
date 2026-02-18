x=int(input("enter your 1st num: "))
y=int(input("enter your second num:  "))
z=int(input("enter your third num:  "))

if(x>y):
    print("x is greater"),
elif(x>z):
    # print("x is greater"),/
elif(y>x):
    print("y is greater"),
elif(y>z):
    print("y is greater"),
elif(z>x):
    print("z is greater "),
elif(z>y):
    print("z is greater"),
else : 
    print("invalid number")
# str = "i am a doctor"
# print (str.find("doctor"))
# str = "I am a student of engineering college"
# print (str.find("student"))
# num = int(input("enter your num"))
# if num%7==0:
#     print("the number is multiple of 7")
# else: print("the number is not multiple of 7")
# student = ["karan",67,"delhi"]
# print (student[0])
# print (len("student"))
# movies = []

# movie1 = (input("enter your 1st movie: "))
# movie2 = (input("enter your 2nd movie: "))
# movie3 = (input("enter your 3rd movie: "))
# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)

# print(movies)

# list1 = [1,2,3]
# list2 = [2,3,1]

# copylist1 = list1.copy()
# copylist1.reverse()

# if(copylist1 == list1):
#     print("palindrome")
# else:print("not palindrome")

# grade =[("c","d","a","b","a","b")]

# # print(grade.count("a"))
# grade.sort

# dictonary = {
#     "table" : ["a piece of furniture","list of facts and figure"],
#     "cat"  : "a small animal"
# }
# print(dictonary)
# subjects = {"python" ,"java" ,"c++" ,"python","java script" ,"java","python" ,"c++" ,"c"  }
# print(len(subjects))
# marks = {}

# x = int(input("enter your phy marks:  "))
# marks.update({"phy":x})

# y= int(input("enter your math marks:  "))
# marks.update({"math":y})

# z = int(input("enter your chem marks:  "))
# marks.update({"chem":z})

# print(marks)
# value = {9,9.0}
# print(value)
# values = {
#     ('flout',9.0),
#     ('int',9)
# }
# print(values)
# i = 5
# while i>= 1:
#     print(i)
#     i-= 1
# nums = {1,4,9,16,25,36,49,64,81,100}
# idx = 0
# while idx <= len(nums)-1:
#     print(idx)
#     idx +=1
# n
# nums = {1,4,9,16,25,36,49,64,81,100,49}
# x = 49

# idx = 0
# for el in nums:
#     if(el == x):
#         print("number found at idx",idx)
#         idx += 1
# seq = range(5)
# for i in seq:
#     print(i)
# n = 5
# sum = 0
# for i in range(n+1):
#     print(i)
#     sum += 1
#     print("total sum: ",sum)

# def func1():
#     try:
#         l = [1,4,5,6,7]
#         i = int(input("Enetr the index: "))
#         print(l[i])
#         return 1
#     except:
#         print("some erroe occurred")
#         return 0
    
#     finally:
#         print("I am always executed")

a = int (input("Enter any value between 5&9")) 

if(a<5 or a<9):
    raise ValueError("Value should be between 5 and 9")




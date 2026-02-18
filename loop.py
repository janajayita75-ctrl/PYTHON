 i = 5
while i>= 1:
   print(i)
    i-= 1
nums = {1,4,9,16,25,36,49,64,81,100}
 idx = 0
 while idx <= len(nums)-1:
    print(idx)
    idx +=1
     n
# # # nums = {1,4,9,16,25,36,49,64,81,100,49}
# # # x = 49

# # # idx = 0
# # # for el in nums:
# # #     if(el == x):
# # #         print("number found at idx",idx)
# # #         idx += 1
# # # seq = range(5)
# # # for i in seq:
# # #     print(i)
# # # n = 5
# # # sum = 0
# # # for i in range(n+1):
# # #     print(i)
# # #     sum += 1
# # #     print("total sum: ",sum)

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


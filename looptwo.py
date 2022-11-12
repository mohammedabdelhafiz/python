# # First challenge

# # def count(num):
# #     new_list = []
# #     for val in range (num,-1,-1):
# #         new_list.append(val)
# #     return new_list
# # print(count(20))

# # Second Challenge

# #Ceate a function that will receive a list with two numbers. Print the first value and return the second.

# # def freturn(the_list):
# #     print(the_list[0])
# #     return the_list[1]
# # print(freturn([3,6]))

# # First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# # Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

# # def first_plus_length(new_listt):
# #     first=new_listt[0]
# #     length=len(new_listt)
# #     total = first + length
# #     return total
# # print(first_plus_length([1,2,3,4,6,54,3,1,5]))

# Values Greater than Second - Write a function that accepts a list and creates a new list
#  containing only the values from the original list that are greater than its 2nd value

# def value_grt_thn_scnd(orig_list):
#     neww_listt = []
#     second_val=orig_list[1]
#     for idx in range(len(orig_list)):
#         if orig_list[idx] > second_val:
#             neww_listt.append(orig_list[idx])
#     print(len(neww_listt))
#     return neww_listt
# print(value_grt_thn_scnd([1,5,8,5,4,7,8,9,0]))

def values(size,value):
    lisstt = []
    for i in range (size):
        lisstt.append(value)
    print(lisstt)

values(7,9)
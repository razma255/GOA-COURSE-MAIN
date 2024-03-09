# #ამოცანა 1

# #ამოცანა 2 

# def multiply(num1, num2):
#     return num1*num2

# print(multiply(12, 100))


# #ამოცანა 3 
# def split_word(word):
#     short = 9999
#     for i in word.split(' '):
#         if len(i) < short:
#             short = len(i)
#     return short

# print(split_word("Let's travel abroad shall we"))


#ამოცანა 4

# def unique_sum(array):
#     unique_arr = []
#     for i in array:
#         if array :
#              unique_arr.append(i)
#     return sum(unique_arr)

# print(unique_sum([4,5,7,5,4,8]))

# # ამოცანა 5

# def max_min(param):
#     arr = param.split(' ')
#     min = 9999
#     max = -9999
#     for i in arr:
#         if int(i) < min:
#             min = int(i)
#         elif int(i) > max:
#             max = int(i)
#     return str(max)+ " " +  str(min)

# print(max_min("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))


#ამოცანა 6
# def range_func(integer, limit):
#     arr = []
#     for i in range(integer,limit,integer):
#         arr.append(i)

#     return arr
# print(range_func(5, 25))


# # ამოცანა 7
# def hashtag_generator(variable):
#     return "#" + "".join([i.capitalize() for i in variable.split(' ')])

# print(hashtag_generator("Hello there thanks for trying my Kata"))


# # # ამოცანა 8

# def arr_zero_last(arr):
#     zero_arr = []
#     other_arr = []
#     for i in arr:
#         if i == 0:
#             zero_arr.append(i)
#         else:
#             other_arr.append(i)
#     return other_arr+zero_arr

# print(arr_zero_last([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))

# # # ამოცანა 9

# def convert(dollar):
#     return str(dollar*6.75) + " Chinese Yuan"

# print(convert(15))
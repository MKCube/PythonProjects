# Take a list, say for example this one:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.
# Extras:
#
# 1) Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# 2) Write this in one line of Python.
# 3) Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

# new_list = []
#
# # for x in a:
# #     if x < 5:
# #         new_list.append(x)
#
print([x for x in a if x < 5])
#
#
# # print("Dej coś")
# number = int(input("Dej coś: "))
# for x in a:
#     if x <= number:
#         new_list.append(x)
# print(new_list)
adi_list = [*range(100)]
#
# # adi_list.reverse()
# adi_list = adi_list[::-1]
#
# print(adi_list)

b = adi_list


def srednia(x: list):
    sr = sum(x) / len(x)
    return sr


average = (srednia(a))
average1 = (srednia(b))

print("Twoja średnia to: ", average)
print("Twoja średnia to: ", average1)

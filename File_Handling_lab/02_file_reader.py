# import os
# from constants import ABSOLUTE_PROJECT_PATH
#
# path = os.path.join(ABSOLUTE_PROJECT_PATH, "numbers.txt")
#
# file = open(path, 'r')
#
# # for line in file:
# #     print(line, end="")
#
# # numbers = [int(el) for el in file.read().split("\n")]
# # print(sum(numbers))
#
# numbers = [int(el) for el in file.read().split("\n")]
# print(sum(numbers))


import os
from constants import   ABSOLUTE_PROJECT_PATH

path = os.path.join(ABSOLUTE_PROJECT_PATH, "numbers.txt")

with open(path, "r") as file:
    numbers = [int(el) for el in file.read().split("\n")]
    print(sum(numbers))
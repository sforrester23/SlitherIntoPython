import sys
from typing import List

file_list = sys.stdin.read().split()

list_four_a_end_ian = [x for x in file_list if x.count("a") == 4 and x[-3:] == "ian"]

print(list_four_a_end_ian)
print(len(list_four_a_end_ian))
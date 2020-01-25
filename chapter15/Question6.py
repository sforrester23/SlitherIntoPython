import sys

file_list = sys.stdin.read().split()
reverse_list = []
alphabet = "abcdefghiyjklmnopqrstuvwxz"

for index in file_list:
    if index[-1] != "z":
        if index[::-1] in file_list[file_list.index(index[-1:]):file_list.index(alphabet[alphabet.find(index[-1])+1])]:
            print(index)
            reverse_list.append(index)
    elif index[-1] == "y" or index[-1] == "i":
        if index[::-1] in file_list[file_list.index(index[-1:]):file_list.index("j")]:
            print(index)
            reverse_list.append(index)
    else:
        if index[::-1] in file_list[file_list.index(index[-1:]):]:
            print(index)
            reverse_list.append(index)

print(reverse_list)
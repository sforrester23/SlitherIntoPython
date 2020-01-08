# string slicer

string_input = input("Input a string please: ")
index1 = int(input("Input an index: "))
index2 = int(input("Input another index: "))

# print("length of string: ", len(string_input))
# print(string_input[0:4])
# print(string_input[-8:-3])
# print(string_input[1:1])
# print(abs(index1))
# print(abs(index1)>len(string_input))

if abs(index1) > len(string_input) or abs(index2) > len(string_input) or index1 == index2:
    print("Can't slice that string...")
else:
    if index1 > index2:
        print(string_input[index2:index1])
    elif index2 > index1:
        print(string_input[index1:index2])

# a recursive function that takes a list of integers as an argument and returns the maxmimum of that list
def maxList(list):
    if len(list) == 1:
        return list[0]
    elif list[0] >= max(list[1:len(list)]):   
        return list[0]
    else:
        return maxList(list[1:len(list)])

print(maxList([0,12,5438,134,13489,81749,478493,2]))

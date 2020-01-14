import sys

with open(sys.argv[1], "r") as inp:
    # read the line from the file how we would like to see it and eventually re-display it
    line = inp.readline()
    # make the line into a list
    # then we can decipher the point at which each separately spaced entry changes from letters to numbers
    line_list = line.split()
    print(line_list)

    # find the point in the list where the letters become numbers and store it as i
    i = 0
    while i < len(line) and line_list[i].isalpha():
        i += 1

    # define an empty dictionary
    dict = {}

    # for each line found, make a dictionary of the key and values
    # This is done by taking the key to be the point in the list up to where we found it became a number
    # the value is the entry in the list after this point (there is only one)

    while line:
        # define the dictionary key value pair for this iteration
        # make the key name from the lists up to the value i

        # count for the loop with j
        j = 0
        # define an empty key variable to begin with
        key = ""
        # loop through j's lower the point of change from letters to numbers
        while j < i:
            # add these word values to the key for each iteration of the loop
            key += line_list[j] + " "
            j += 1
        # make the dictionary entry based on the constructed key and the number entry for value
        dict[key.strip()] = line_list[i]

        # repeat the file information gathering procedure
        line = inp.readline()
        line_list = line.split()
        i = 0
        while i < len(line) and line_list[i].isalpha():
            i += 1

    # assemble the key value pairs to print in a nice format
    for (k, v) in dict.items():
        print("{:>15} : {:<15}".format(k, v))


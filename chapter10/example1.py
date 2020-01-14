import sys

src = sys.argv[1]  # The input source file
dst = sys.argv[2]  # The file to output to

with open(src, 'r') as fin, open(dst, 'a') as fout:  # Open in append mode

    student = fin.readline().strip()  # Strip the newline character
    while student:

        student_data = student.split()  # ['Liam', '84'] for example

        name = student_data[0]
        mark = int(student_data[1])

        if mark < 40:
            grade = "FAIL"
        else:
            grade = "PASS"

        fout.write('{:s} {:s}\n'.format(name, grade))  # Write to the output file

        student = fin.readline().strip()  # Get the next student
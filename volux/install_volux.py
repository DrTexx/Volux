filename="testfile.txt"
def return_each_line(file):
    with open(filename) as f:
        lines = return_each_line(f)
        return([line_terminated.rstrip('\n') for line_terminated in file])
    print(lines)
    
def read_file(filename):
    text_file = open(filename+".txt", "r")
    lines = text_file.read().split(',')
    print lines
    print len(lines)
    text_file.close()

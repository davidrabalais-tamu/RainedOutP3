FILE_NAME = './log.txt'

# Use open() to get a filehandle that can access the file
fh = open(FILE_NAME)

# Loop through the file 
# for line in fh:
#   print(line)

# The filehandle object provides many basic file operations:
# fh.read(64)     # read the specified bytes from the file (if no byte size is specified, then the entire file is read)
# fh.readline()   # read a single line from the file (up to a newline character - \n)
# fh.write('some data here')  # write a string to the file (make sure the file was open()'ed for writing!)


array = ["Oct", "Nov", "Dec", "Jan", "Feb", "Mar"]
six_mo =0
total_lines= 0
total_requests= 0
# Alternately, skip the assignment to the filehandle altogether:
for line in open(FILE_NAME):
    total_lines += 1
    if "GET" in line:
        total_requests+= 1
#       print(line)
        for month in array:
            if month in line:
                six_mo += 1

# The loop example above is memory-efficient, and also easy to read
print("number of requests made in first six months is ", six_mo)
print("number of lines ", total_lines)
print("number of total requests ", total_requests)
fh.close()      # close the file when you're finished with it
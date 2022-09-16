with open(r"412Project3.txt", 'r') as fp:
    count = 0
    for line in fp:
        if line != "\n":
            count += 1

print('Total Number of Lines', count)

words = ["Oct/1995", "Sep/1995", "Aug/1995", "Jul/1995", "Jun/1995", "May/1995"]
count =0
with open(r'412Project3.txt', 'r') as fp:
    lines = fp.readlines()
    for line in lines:
        if any(words in line for words in words):
            count += 1 
print('Total Requests in the 6 months', count)
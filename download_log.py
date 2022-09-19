#copied from Kayla's and Katherine's repository
#!/usr/bin/python
with open(r"TCMG412Lab3.txt", 'r') as fp:
	lines = len(fp.readlines())
	print('Total Number of lines:', lines)

#from cgitb import lookup
#import re


#for search_name in ['Oct', 'Sep', 'Aug', 'Jul', 'Jun', 'May']:
 ##print(f"Search Result for {search_name}")
  #if found:
   # name = found
   # print(f"Name: {name}")
 # else:
  #  print(f"{search_name} not found")

 # print("")

file = open('TCMG412Lab3.txt','r')

words = ["Oct/1995:", "Sep/1995:", "Aug/1995:", "Jul/1995:", "Jun/1995:", "May/1995:"]
count=0
lines=file.readlines()
for line in lines:
    if any(word in line for word in words):
        count+=1 
print('Total requests that have been made in the past 6 months: ', count)

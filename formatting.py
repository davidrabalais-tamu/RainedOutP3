from tabulate import tabulate
mydata = [("requests in the first 6 months", six_mo ), ("total requests", total_requests)]
headers = ["Type of Requests" , "Results"]

print = (tabulate(mydata, headers=headers, tablefmt="grid"))

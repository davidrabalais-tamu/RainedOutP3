from tabulate import tabulate
  mydata = [{"six_mo", "total_requests"}]
  headers = ["Past 6 months" , "Total requests"]

  print = (tabulate(mydata, headers=headers, tablefmt="grid"))
# 
# Group Project 3 - Pulling down the log file
#
import urllib.request
url = "https://s3.amazonaws.com/tcmg476/http_access_log"

def main():
  # open a connection to a the log files URL
  webUrl = urllib.request.urlopen(url)
  response = urllib.request.urlretrieve(url, "log.log")
  # Save the contents of the log


  # get the result code and print it
  print ("result code: " + str(webUrl.getcode()))
  htmltext = webURL.read()
  webURL.close()

  for t in htmltext:
    print t + "\n"
  
  # read the data from the URL and print it
  data = webUrl.read()
  print (data)

if __name__ == "__main__":
  main()
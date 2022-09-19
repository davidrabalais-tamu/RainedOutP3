print ('This is the program for Group 6 Project #3\r\n')
print('If you have\'t already, please install tabulate with the following command before proceeding.\r\n\npip3 install tabulate\n')
input('Press ENTER to continue or CTRL+C to quit...')
print ('Downloading the log file...')
import download_log
print ('\n \nParsing the log file and counting number of requests')
import parsing
print ('\n \nFormatting Output')
import formatting
import csv
import rtfunicode
from striprtf import rtf_to_text
import striprtf
import extract_rtf
import re

fr = open("results.csv",'a')
# with open("sample.csv", encoding='utf-8') as csvfile:
#      csvreader = csv.reader(csvfile, delimiter=",")
#      for line in csvreader:
# #             #print(" ".join(line))
#             converted=rtf_to_text(csvfile.read()).split(',,')
#             print ("".join(converted))
#             f.write("".join(converted))


f = open("sample.csv", "r")
#for line in f:
#print(rtf_to_text(f.read()).split(',,')[1].replace('\n,',''))
converted_list= rtf_to_text(f.read()).split(',,')
for i in converted_list:
   print(i.replace('\n,', '').strip('\n'))
   result=i.replace('\n,', '').strip('\n')
   fr.write(result+"\n")



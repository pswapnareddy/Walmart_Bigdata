import csv
import os
import json

# Before running the Script, Make sure to have the input tab file
#Also, make sure to have the hive table script 

print '***************** Process Started *********************'
print
print
print '   Converting CSV file to Json   '
os.system('rm -rf /home/cloudera/json_data.json')
csv_data = r"csv_converted.csv"
json_data = r"json_data.json"

print 'CSV File:',csv_data
print 'Json File:',json_data

csvfile = open(csv_data, 'r')
jsonfile = open(json_data, 'w')

fieldnames = ("id","name","salary")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')

csvfile.close()
jsonfile.close()

print 
print '   Conversion Completed   '
print 
print
print 'Now Loading the data from local into Hive Table'
print 'Running the Shell Process to load the dataset into HDFS'
os.system('hadoop fs -mkdir -p /home/cloudera/myjsontable/')
os.system("hadoop fs -rm -r /home/cloudera/myjsontable/* >> /dev/null")
os.system('hadoop fs -put /home/cloudera/json_data.json /home/cloudera/myjsontable/')
os.system("hive -S -f /home/cloudera/create_json.hql >> /dev/null")
print 'Data Loading Completed in Hive'
print
print 
print '************** Process End *********************

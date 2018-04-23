import csv
import os

# Before running the Script, Make sure to have the input tab file
#Also, make sure to have the hive table script 

print '***************** Process Started *********************'
print
print
print '   Converting Tab seperated to CSV   '
os.system('rm -rf /home/cloudera/csv_converted.txt')
text_data = r"test.txt"
csv_data = r"csv_converted.csv"

print 'Text File:',text_data
print 'CSV File:',csv_data

with open(text_data, "r") as in_text:
    in_reader = csv.reader(in_text, delimiter = '\t')
    with open(csv_data, "w") as out_csv:
        out_writer = csv.writer(out_csv)
        for row in in_reader:
            out_writer.writerow(row)

in_text.close()
out_csv.close()

print 
print '   Conversion Completed   '
print 
print
print 'Now Loading the data from local into Hive Table'
print 'Running the Shell Process to load the dataset into HDFS'
os.system('hadoop fs -mkdir -p /home/cloudera/mytable/')
os.system("hadoop fs -rm -r /home/cloudera/mytable/* >> /dev/null")
os.system('hadoop fs -put /home/cloudera/csv_converted.csv /home/cloudera/mytable/')
os.system("hive -S -f /home/cloudera/create.hql >> /dev/null")
print 'Data Loading Completed in Hive'
print
print 
print '************** Process End *********************'


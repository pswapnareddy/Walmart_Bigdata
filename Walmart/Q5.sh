5)
# DDL for table test
# create external table test (age int, name string)
# ROW FORMAT DELIMITED
# FIELDS TERMINATED BY ','
# STORED AS TEXTFILE
# location '/user/home/cloudera/test/';

echo "Running hadoop copy command"
echo "hadoop fs -put test.txt /user/home/cloudera/test/"
# Command to put file in hdfs directory of the hive table.
hadoop fs -put test.txt /user/home/cloudera/test/


echo "Running hive table count "
echo 'hive -e "select count(*) from default.test;"'
# Hive command to get count of the table
hive -e "select count(*) from default.test;"


echo "Running hive command to get length of column"
echo 'hive -e  "select length(name) from test;"'

# Hive command to get length of  name column the table
hive -e  "select length(name) from test;"

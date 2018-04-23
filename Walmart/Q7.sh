7)

echo "Running hive insert script "
# Insert hql file--> insert into or overwrite final_table select * from stage_table

hive -f Insert.hql

echo "Running hadoop remove command to delete stage data"
# Command to remove stage data
hadoop fs -rm /user/home/clouera/test/test.txt

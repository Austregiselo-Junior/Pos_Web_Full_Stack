
 # This code is sample code, provided as-is, and we make no
 # warranties as to its correctness or suitability for
 # any purpose.
 #
 # We hope that it's useful to you.  Enjoy.
 # Copyright LearningPatterns Inc.


# DONE: finish imports.
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Usage:
# spark-submit  --master spark://localhost:7077  <lab-root>/src/main/scala/ProcessFiles.py <files to process>
# 
# Multiple files can be specified with a space between the file paths.
# Examples of files are:
#                             /etc/hosts
#                             ~/spark-labs/data/twinkle/500M.data
#                             s3n://elephantscale-public/data/twinkle/100M.data
#                             tachyon://tachyon_ip_address:19998/file
# 
# e.g:
# - with 4G executor memory and turning off verbose logging
#     spark-submit --class com.mycompany.ProcessFiles  --master spark://localhost:7077 --executor-memory 4g   --driver-class-path logging/   target/scala-2.11/myapp_2.11-1.0.jar  ~/spark-labs/data/twinkle/1G.data
# 

if __name__ == "__main__":
	"""
		Usage: ProcessFiles fileName(s)
	"""
	"""
	if len(sys.argv) < 1:
		print "need file(s) to load"
		sys.exit()
	"""

	# DONE: Create a SparkSession
	spark = SparkSession.builder.appName("Process Files").getOrCreate()
    # We'll set master from spark-submit, so don't set it here.
	
	# Loop through file names, skipping the first arg (name of program)
	iterfiles = iter(sys.argv)
	next(iterfiles)
	for file in iterfiles:
		# DONE: create a DataFrame from the file (assume it is text)
		fileDF = spark.read.text(file)
		# DONE: count # of elements in the dataframe.
		count =  fileDF.count()
		
		# Print out result
		print("### %s: count:  %s " % (file,count))
		
		# Do this so the 4040 UI stays alive - bit of a hack, but useful for us.
		print("Hit ^C to terminate the program...:")
		# response = raw_input(">>>")

		# spark.stop()
		
	
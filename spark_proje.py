# To find out path where pyspark installed
import findspark
findspark.init()

# Create SparkSession and sparkcontext
from pyspark.sql import SparkSession
spark = SparkSession.builder\
                    .master("local")\
                    .appName('Firstprogram')\
                    .getOrCreate()
sc=spark.sparkContext

# Read the input file and Calculating words count
text_file = sc.textFile("new.txt")
counts = text_file.flatMap(lambda line: line.split(" ")) \
                            .map(lambda word: (word, 1)) \
                           .reduceByKey(lambda x, y: x + y)

# Printing each word with its respective count
output = counts.collect()
for (word, count) in output:
    print("%s: %i" % (word, count))
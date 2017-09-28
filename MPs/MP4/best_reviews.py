from pyspark import SparkContext, SparkConf
import sys
if len(sys.argv) != 3:
    print("Usage: best_reviews.py INPUT OUTPUT")
    sys.exit()

input_file = sys.argv[1]
output_file = sys.argv[2]

conf = SparkConf().setAppName("best_reviews")
sc = SparkContext(conf=conf)

reviews = sc.textFile(input_file)

# After you're done:
# <RDD>.saveAsTextFile(output_file)

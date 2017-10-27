from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext, SparkSession
conf = SparkConf().setAppName("Jaunting With Joins")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)
spark = SparkSession.builder.getOrCreate()

reviews = spark.read.json("hdfs:///shared/yelp/review.json")
businesses = spark.read.json("hdfs:///shared/yelp/business.json")
checkins = spark.read.json("hdfs:///shared/yelp/checkin.json")
users = spark.read.json("hdfs:///shared/yelp/user.json")

sqlContext.registerDataFrameAsTable(reviews, "reviews")
sqlContext.registerDataFrameAsTable(businesses, "businesses")
sqlContext.registerDataFrameAsTable(checkins, "checkins")
sqlContext.registerDataFrameAsTable(users, "users")

# Do your queries here

# CHANGE THESE TO YOUR ANSWERS
query_1_state = ""
query_2_maximum_funny = 123
query_3_user_ids = [123, 456, 789]

# DON'T EDIT ANYTHING BELOW THIS COMMENT
with open('jaunting_with_joins.txt', 'w+') as f:
    f.write('1: {}\n'.format(query_1_state))
    f.write('2: {}\n'.format(query_2_maximum_funny))
    f.write('3: {}\n'.format(','.join(map(str, query_3_user_ids))))
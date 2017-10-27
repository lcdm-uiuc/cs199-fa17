from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext
import csv
conf = SparkConf().setAppName("Aggregation Aggravation")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)
schema = "Id,ProductId,UserId,ProfileName,HelpfulnessNumerator,HelpfulnessDenominator,Score,Time,Summary,Text".split(',')


def parse_csv(x):
    x = x.encode('ascii', 'ignore').replace('\n', '')
    d = csv.reader([x])
    return next(d)

reviews = sc.textFile("hdfs:///shared/amazon/amazon_food_reviews.csv")
first = reviews.first()
csv_payloads = reviews.filter(lambda x: x != first).map(parse_csv)

df = sqlContext.createDataFrame(csv_payloads, schema)
sqlContext.registerDataFrameAsTable(df, "amazon")

# Do your queries here

# CHANGE THESE TO YOUR ANSWERS
query_1_num_reviews= 123
query_1_user_id = 123
query_2_product_ids = [123, 456]
query_3_product_ids = [123, 456]

# DON'T EDIT ANYTHING BELOW THIS COMMENT
with open('aggregation_aggravation.txt', 'w+') as f:
    f.write("1: {}, {}\n".format(query_1_num_reviews, query_1_user_id))
    f.write('3: {}\n'.format(','.join(map(str, query_2_product_ids))))
    f.write('3: {}\n'.format(','.join(map(str, query_3_product_ids))))

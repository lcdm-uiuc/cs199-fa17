import csv
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext
conf = SparkConf().setAppName("Quizzical Queries")
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

# Do your queries here

# CHANGE THESE TO YOUR ANSWERS
query_1_review_string = "FOOBAR"
query_2_five_star_ratings = 123
query_3_user_count = 123

# DON'T EDIT ANYTHING BELOW THIS COMMENT
with open('quizzical_queries.txt', 'w+') as f:
    f.write("1: '{}'\n".format(query_1_review_string))
    f.write("2: {}\n".format(query_2_five_star_ratings))
    f.write('3: {}\n'.format(query_3_user_count))
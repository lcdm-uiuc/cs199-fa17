from pyspark import SparkContext, SparkConf
conf = SparkConf().setAppName("Amazon Helpfulness Regression")
sc = SparkContext(conf=conf)

reviews = sc.textFile("gs://dataproc-3ba9e17b-802e-4fec-8f2d-4e0d4167cadb-us-central1/Datasets/amazon/amazon_food_reviews.csv")

with open('amazon_helpfulness_regression.txt', 'w+') as f:
    pass

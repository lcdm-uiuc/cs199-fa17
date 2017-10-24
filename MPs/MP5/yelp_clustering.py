from pyspark import SparkContext, SparkConf
conf = SparkConf().setAppName("Yelp Clustering")
sc = SparkContext(conf=conf)

businesses = sc.textFile("gs://dataproc-3ba9e17b-802e-4fec-8f2d-4e0d4167cadb-us-central1/Datasets/yelp/business.json")

with open('yelp_clustering.txt', 'w+') as f:
    pass

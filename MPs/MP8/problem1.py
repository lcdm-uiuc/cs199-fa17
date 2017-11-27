from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext

conf = SparkConf().setAppName("Popular hashtags")
sc = SparkContext(conf=conf)
ssc = StreamingContext(sc, 10)
ssc.checkpoint('streaming_checkpoints')

tweet_stream = ssc.socketTextStream("nebula-m", 8001)

# YOUR CODE HERE

ssc.start()
ssc.awaitTermination()

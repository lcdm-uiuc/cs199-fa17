from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext

conf = SparkConf().setAppName("Reddit bot detector")
sc = SparkContext(conf=conf)
ssc = StreamingContext(sc, 10)
ssc.checkpoint('streaming_checkpoints')

reddit_comment_stream = ssc.socketTextStream("nebula-m", 8000)

# YOUR CODE HERE

ssc.start()
ssc.awaitTermination()

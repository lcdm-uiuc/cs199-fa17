# MP 8: Introduction to Spark Streaming

## Introduction

This MP will introduce Spark Streaming. You will be writing some simple Spark jobs that process streaming data from Twitter and Reddit.

### Example

Here's an example of a Spark Streaming application that does "word count" on incoming Tweets

```python
import json
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext

# Initialize the spark streaming context
conf = SparkConf().setAppName("Word count")
sc = SparkContext(conf=conf)
ssc = StreamingContext(sc, 10)
ssc.checkpoint('streaming_checkpoints')

# Stream window tunable parameters
window_length = 900 # The size of each window "slice" to consider
slide_interval = 30 # How often the windowed function is executed


# Parse tweets and return the text's word count
def get_tweet_word_count(tweet_json):
    data = json.loads(tweet_json)
    return len(data['text'].split(' '))


# Listen to the tweet stream
tweet_json_lines = ssc.socketTextStream("nebula-m", 8001)

# Map json tweets to word counts
tweet_word_counts = tweet_json_lines.map(get_tweet_word_count)

# Do a windowed aggregate sum on the word counts
windowed_word_count = tweet_word_counts.reduceByWindow(lambda x, y: x + y, window_length, slide_interval)

# Save output to Hadoop
windowed_word_count.saveAsHadoopFiles('tweet_word_count')


# Signal to spark streaming that we've setup our streaming application, and it's ready to be run
ssc.start()

# Run the streaming application until it's terminated externally
ssc.awaitTermination()
```

### Resources

For this MP, you'll find the following Resouces useful:

* [Spark Streaming Programming Guide](https://spark.apache.org/docs/2.1.0/streaming-programming-guide.html)
* [Spark Streaming API Documentation](https://spark.apache.org/docs/2.1.0/api/python/pyspark.streaming.html)

### Setup

Download and install the version of Terraform for your system from [this page](https://www.terraform.io/downloads.html).

## MP Activities

### Problem 1 - Popular Hashtags

Write a Spark Streaming application that listens to an incoming stream of Tweets and counts the number of times each Hashtag is used within a given stream interval.

For example, if we saw a stream like this:
```
Testing my cool application #HelloWorld
#HelloWorld Foo #Bar
Here's another Tweet #HelloWorld
```

Then our hashtag count would look like this:

```
("#HelloWorld", 3)
("#Bar", 1)
```

For this problem, use a window length of **60 seconds** with a slide interval of **30 seconds**.

### Problem 2 - Subreddit Most Common Words

Note that Reddit comments have a field called "subreddit" that indicates on which forum on Reddit the comments were posted. Write a Spark Streaming application that listens to an incoming stream of Reddit comments and outputs the **top 10** most used word in comments **per each subreddit**. Normalize the comments by transforming them to all lowercase, and use the "stopwords" provided in the solution template to remove common words.

For this problem, use a window length of **900 seconds** with a slide interval of **300 seconds**.

### Problem 3 - Reddit Bot Detection

Write a Spark Streaming application that listens to an incoming stream of Reddit comments and detects users that post multiple similar comments within a given stream period.

A user should be reported as a "bot" if their comments within a given stream window fulfill all these criteria:

- The user has made at least **5** comments within the given window.
- The user has made a comment that is within **0.25** similarity to at least half of all other comments that user made in the given window. Use [difflib.get_close_matches](https://docs.python.org/2/library/difflib.html#difflib.get_close_matches) to determine string similarity

The output of your program should be a list of users that have comment histories matching the above criteria.

(To sanity-check your output, you should probably see the "AutoModerator" user as a bot after your job has been running for a few minutes)

For this problem, use a window length of **900 seconds** with a slide interval of **300 seconds**.

## Stream Formats

### Twitter

You will receive Tweets as a JSON blob with the following schema:

```
{
    "text": "<tweet body>"
}
```

This stream can be accessed via TCP on `nebula-m:8001` from within the cluster.

If you want to look at the raw stream, you can do so by running `telnet nebula-m 8001` on the GCP cluster

### Reddit

You will receive Reddit comments as a JSON blob with the following schema:

```
{
    "text": "<comment body>",
    "subreddit": "<subreddit name>",
    "author": "<comment author>"
}
```

This stream can be accessed via TCP on `nebula-m:8000` from within the cluster.

If you want to look at the raw stream, you can do so by running `telnet nebula-m 8000` on the GCP cluster

### Tips

You can "listen" to the stream by running `telnet <stream_address> <stream_port>`. Spark Streaming considers each line as a distinct record, so you'll see a JSON blob on each line.

## Deliverables
**MP 8 is due on Saturday, December 2nd, 2017 at 11:55PM.**

Please zip your source files for the following exercises and upload it to Moodle (learn.illinois.edu).

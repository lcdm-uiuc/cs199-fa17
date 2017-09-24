# MP 3: Hadoop Map/Reduce on "Real" Data

## Introduction
In the past 2 labs, you were introduced to the concept of Map/Reduce and how we can execute Map/Reduce Python scripts on Hadoop with Hadoop Streaming.

This week, we'll give you access to a modestly large (~60GB) Twitter dataset. You'll be using the skills you learned in the last two weeks to perform some more complex transformations on this dataset.

Like in the last MP, we'll be using Python to write mappers and reducers. We've included a helpful shell script to make running mapreduce jobs easier. The script is in your `bin` folder, so you can just run it as `mapreduce`, but we've included the source in this MP so you can see what it's doing.

Here's the usage for that command:

```
Usage: ./mapreduce map-script reduce-scripe hdfs-input-path hdfs-output-path

Example: ./mapreduce mapper.py reducer.py /tmp/helloworld.txt /user/quinnjarr
```

## The Dataset

The dataset is located in `/shared/snapTwitterData` in HDFS. You'll find these files: 

```
/shared/snapTwitterData/tweets2009-06.tsv
/shared/snapTwitterData/tweets2009-07.tsv
/shared/snapTwitterData/tweets2009-08.tsv
/shared/snapTwitterData/tweets2009-09.tsv
/shared/snapTwitterData/tweets2009-10.tsv
/shared/snapTwitterData/tweets2009-11.tsv
/shared/snapTwitterData/tweets2009-12.tsv
```

Each file is a `tsv` (tab-separated value) file. The schema of the file is as follows:

```
POST_DATETIME <tab> TWITTER_USER_URL <tab> TWEET_TEXT
```

Example:

```
2009-10-31 23:59:58	http://twitter.com/sometwitteruser	Wow, CS199 is really a good course
```
	
## MP Activities
**MP 3 is due on Wednesday, September 27th, 2017 at 11:55PM.**

Please zip your source files for the following exercises and upload it to Moodle (learn.illinois.edu).

1. Write a map/reduce program to determine the the number of @-replies each user received. You may assume a tweet is an @-reply iff the tweet starts with an `@` character. You may also assume that each @-reply is only a reply to a single user. (i.e. `@foo @bar hello world` is an @-reply to `@foo`, but not `@bar`) Your output should be in this format (space-separated):

	```
	<USER_HANDLE  (Including @ symbol)> <NUMBER_REPLIES_RECEIVED>

	Example:
	@jack 123
	```

2. Write a map/reduce program to determine the user with the most Tweets for every given day in the dataset. (If there's a tie, break the tie by sorting alphabetically on users' handles) Your output should be in this format (space-separated):

	```
	<YYYY-MM-DD> <USER_HANDLE (Including @ symbol)>

	Example:
	2016-01-01 @jack
	```

3. Write a map/reduce program to determine the size of each users' vocabulary -- that is, determine the number of unique words used by each user accross all their Tweets. For the purposes of this problem, you should use the `.split()` method to split each Tweet into words. Your output should be in this format (space-separated):

	```
	<USER_HANDLE> <NUMBER_OF_WORDS>

	Example:
	@jack 123
	```


### Don't lose your progress!

Hadoop jobs can take a very long time to complete. If you don't take precautions, you'll lose all your progress if something happens to your SSH session.

To mitigate this, we have installed `tmux` on the cluster. Tmux is a tool that lets us persist shell sessions even when we lose SSH connection.

1. Run `tmux` to enter into a tmux session.
2. Run some command that will take a long time (`ping google.com`)
3. Exit out of your SSH session.
4. Log back into the server and run `tmux attach` and you should find your session undisturbed.

### Suggested Workflow

1. Write your map/reduce and test it with regular unix commands:

	```
	head -n 10000 /mnt/volume/snapTwitterData/tweets2009-06.tsv | ./<MAPPER>.py | sort | ./<REDUCER>.py
	```

2. Test your map/reduce with a single Tweet file on Hadoop:

	```
	hdfs dfs -mkdir -p twitter
	hdfs dfs -rm -r twitter/out
	mapreduce_streaming <MAPPER>.py <REDUCER>.py /shared/snapTwitterData/tweets2009-06.tsv twitter/out
	```
	
3. Run your map/reduce on the full dataset:
	```
	hdfs dfs -mkdir -p twitter
	hdfs dfs -rm -r twitter/out
	mapreduce_streaming <MAPPER>.py <REDUCER>.py /shared/snapTwitterData/*.tsv twitter/out
	```

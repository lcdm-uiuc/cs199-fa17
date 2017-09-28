# MP 4: Spark

## Introduction

As we have talked about in lecture, Spark is built on the concept of a *Resilient Distributed Dataset* (RDD). 

PySpark allows us to interface with these RDD’s in Python. Think of it as an API. In fact, it is an API: it even has its own [documentation](http://spark.apache.org/docs/latest/api/python/)! It’s built on top of the Spark’s Java API and exposes the Spark programming model to Python.

PySpark makes use of a library called `Py4J`, which enables Python programs to dynamically access Java objects in a Java Virtual Machine.

This allows data to be processed in Python and cached in the JVM. This model lets us combine the performance of the JVM with the expressiveness of Python.


## Running your Jobs

We'll be using `spark-submit` to run our spark jobs on the cluster. `spark-submit` has a couple command line options that you can tweak.

#### `--master`
This option tells `spark-submit` where to run your job, as Spark can run in several modes.

* `local`
    * The Spark job runs locally, *without* using any compute resources from the cluster.
* `yarn-client`
    * The spark job runs on our YARN cluster, but the driver is local to the machine, so it 'appears' that you're running the job locally, but you still get the compute resources from the cluster. You'll see the logs spark provides as the program executes.
    * When the cluster is busy, you *will not* be able to use this mode, because it imposes too much of a memory footprint on the node that everyone is SSH'ing into.
* `yarn-cluster`
    * The spark job runs on our YARN cluster, and the spark driver is in some arbitrary location on the cluster. This option doesn't give you logs directly, so you'll have to get the logs manually.
    * In the output of `spark-submit --master yarn-cluster` you'll find an `applicationId`. (This is similar to when you ran jobs on Hadoop). You can issue this command to get the logs for your job:

        ```
        yarn logs -applicationId <YOUR_APPLICATION_ID> | less
        ```
    * When debugging Python applications, it's useful to `grep` for `Traceback` in your logs, as this will likely be the actual debug information you're looking for.

        ```
        yarn logs -applicationId <YOUR_APPLICATION_ID> | grep -A 50 Traceback
        ```
        
    * *NOTE*: In cluster mode, normal "local" IO operations like opening files will behave unexpectedly! This is because you're not guaranteed which node the driver will run on. You must use the PySpark API for saving files to get reliable results. You also have to coalesce your RDD into one partition before asking PySpark to write to a file (why do you think this is?). Additionally, you should save your results to HDFS.

        ```python
        <my_rdd>.coalesce(1).saveAsTextFile('hdfs:///user/MY_USERNAME/foo')
        ```

#### `--num-executors`
This option lets you set the number of executors that your job will have. A good rule of thumb is to have as many executors as the maximum number of partitions an RDD will have during a Spark job (this heuristic holds better for simple jobs, but falls apart as the complexity of your job increases).

The number of executors is a trade off. Too few, and you might not be taking full advantage of Spark's parallelism. However, there is also an upper bound on the number of executors (for obvious reasons), as they have a fairly large memory footprint. (Don't set this too high or we'll terminate your job.)

You can tweak executors more granularly by setting the amount of memory and number of cores they're allocated, but for our purposes the default values are sufficient.

### Putting it all together

Submitting a spark job will usually look something like this:

```
spark-submit --master yarn-cluster --num-executors 10 <my_spark_job>.py <job_arguments>
```

Be sure to include the `--master` flag, or else your code will only run locally, and you won't get the benefits of the cluster's parallelism.

### Interactive Shell

While `spark-submit` is the way we'll be endorsing to run PySpark jobs, there is an option to run jobs in an interactive shell. Use the `pyspark` command to load into the PySpark interactive shell. You can use many of the same options listed above to tweak `pyspark` settings, such as `--num-executors` and `--master`.

Note: If you start up the normal `python` interpreter on the cluster, you won't be able to use any of the PySpark features.

### Helpful Hints

* You'll find the [PySpark documentation](https://spark.apache.org/docs/2.0.0/api/python/pyspark.html#pyspark.RDD) (especially the section on RDDs) **very** useful.
* Run your Spark jobs on a subset of the data when you're debugging. Even though Spark is very fast, jobs can still take a long time - especially when you're working with the review dataset. When you are experimenting, always use a subset of the data. The best way to use a subset of data is through the [take](https://spark.apache.org/docs/1.6.2/api/java/org/apache/spark/rdd/RDD.html#take(int)) command.

Specifically the most common pattern to sample data looks like
`rdd = sc.parallelize(rdd.take(100))`
This converts an rdd into a list of 100 items and then back into an RDD through the `.parallelize` function.

* [Programming Guide](http://spark.apache.org/docs/latest/programming-guide.html) -- This documentation by itself could be used to solve the entire MP. It is a great quick-start guide about Spark.


## The Dataset

This week, we'll be working off of a set of released Yelp data.

The dataset is located in `/shared/yelp` in HDFS. We'll be using the following files for this MP:

```
/shared/yelp/yelp_academic_dataset_business.json
/shared/yelp/yelp_academic_dataset_checkin.json
/shared/yelp/yelp_academic_dataset_review.json
/shared/yelp/yelp_academic_dataset_user.json
```

We'll give more details about the data in these files as we continue with the MP, but the general schema is this: each line in each of these JSON files is an independent JSON object that represents a *distinct entity*, whether it be a business, a review, or a user.

*Hint:* JSON is parsed with `json.loads`

## MP Activities
**MP 4 is due on Wednesday, October 4th, 2017 at 11:55PM.**

Please zip your source files for the following exercises and upload it to Moodle (learn.illinois.edu).

**IMPORTANT:** To grade your code, we may use different datasets than the ones we have provided you. In order to receive credit for this assignment, you **must** accept an argument in your job. This single argument will be the location of the dataset. Note that the starting code for this MP already has this implemented.

### 1. Least Expensive Cities

This problem uses the `yelp_academic_dataset_business.json` dataset.

In planning your next road trip, you want to find the cities that will be the least expensive to dine at.

It turns out that Yelp keeps track of a handy metric for this, and many restaurants have the attribute `RestaurantsPriceRange2` that gives the business a score from 1-4 as far as 'priciness'.

Write a PySpark application that sorts cities by the average 'priciness' of their businesses/restaurants.

Notes:

* Discard any business that does not have the `RestaurantsPriceRange2` attribute
* Discard any business that does not have a valid city and state
* Your output should be sorted descending by average price (highest at top, lowest at bottom). Your average restaurant price should be rounded to 2 decimal places. Each city should get a row in the output and look like:

    ```
    CITY, STATE: PRICE

    Example:

    Champaign, IL: 1.23
    ```

### 2. Best Reviews

This problem uses the `yelp_academic_dataset_review.json` dataset.

In selecting a restaurant, you might want to find the review that Yelp users have decided is the best review. For each business in the `review` dataset, find the review that has the greatest engagement. That is, find the review that has the greatest `useful` + `funny` + `cool` interactions. These are fields of the review

Your output should should look like this:

    ```
    BUSINESS_ID REVIEW_ID

    Example: 
    KYasaF1nov1bn7phfSgWeg EmuqmSacByt96t8G5GK0KQ
    ```

### 3. Yelp Reviewer Accuracy

For this activity, we'll be looking at [Yelp reviews](https://www.youtube.com/watch?v=QEdXhH97Z7E). 😱 Namely, we want to find out which Yelp reviewers are... more harsh than they should be.

To do this we will calculate the average review score of each business in our dataset, and find how far away users' ratings are from the average of a business.
 
The `average_business_rating` of a business is the sum of the ratings of the business divided by the count of the ratings for that business. A user's review offset score is the sum of the differences between their rating and the average business rating. A positive score indicates that a user tends to give higher ratings than the average; a negative score indicates that the user tends to give lower ratings than the average.

Your output should look like this:
```
user_id: average_review_offset
```

Your output should first list the users with the top 100 positive review offsets, then the users with the top 100 negative review offsets (by magnitude).

Notes:

* Business have "average rating" as a property. We **will not** be using this. Instead - to have greater precision - we will be manually calculating a business' average reviews by averaging all the review scores given in `yelp_academic_dataset_review.json`.
* Discard any reviews that do not have a rating, a `user_id`, and a `business_id`.

### 4. Descriptors of a Good Business

Suppose we want to predict a review score from its text. There are many ways we could do this, but a simple way would be to find words that are indicative of either a positive or negative review.

In this activity, we want to find the words that are the most positively 'charged'. We can think about the probability that a word shows up in a review as depending on the type of a review. For example, it is more likely that "delicious" would show up in a positive review than a negative one.

Calculate the probability of each word appearing to be the number of occurrences of the word in the category tested (positive/negative) divided by the number of reviews in that category.

For example, if we had a dataset of the following reviews:

```
1 star: The food was delicious, but everything else was bad.
5 star: Everything was delicious!
4 star: I liked the food, it was delicious.
3 star: Meh, it was OK.
```

We see that `delicious` appears in `1` negative review, and `2` positive reviews. We have `1` total negative review, and `3` positive reviews. `P(positive) = 0.666` and `P(negative) = 0.5` (not realistic, of course). Our `probability_diff` for 'delicious' would therefore be `0.666 - 0.5 = 0.166`.

Output the **top 250** words that are most likely to be in positive reviews, but not in negative reviews (maximize `P(positive) - P(negative)`).

Notes:

* Consider a review to be positive if it has `>=3` stars, and consider a review negative if it has `<3` stars.
* Your output should be as follows, where `probability_diff` is `P(positive) - P(negative)` rounded to **4** decimal places and sorted in descending order:

    ```
    word: probability_diff

    Example:
    delicious 0.1234
    ```

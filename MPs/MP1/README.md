# MP 1: Introduction to MapReduce

## Introduction

This MP will introduce the map/reduce computing paradigm. In essence, map/reduce breaks tasks down into a map phase (where an algorithm is mapped onto data) and a reduce phase, where the outputs of the map phase are aggregated into a concise output. The map phase is designed to be parallel, so as to allow wide distribution of computation.

The map phase identifies keys and associates with them a value. The reduce phase collects keys and aggregates their values. The standard example used to demonstrate this programming approach is a word count problem, where words (or tokens) are the keys and the number of occurrences of each word (or token) is the value.

As this technique was popularized by large web search companies like Google and Yahoo who were processing large quantities of unstructured text data, this approach quickly became popular for a wide range of problems. The standard MapReduce approach uses Hadoop, which was built using Java. However, to introduce you to this topic without adding the extra overhead of learning Hadoop's idiosyncrasies, we will be 'simulating' a map/reduce workload in pure Python.

## Example: Word Count

This example displays the type of programs we can build from simple map/reduce functions. Suppose our task is to come up with a count of the occurrences of each word in a large set of text. We could simply iterate through the text and count the words as we saw them, but this would be slow and non-parallelizable.

Instead, we break the text up into chunks, and then split those chunks into words. This is the ‘map’ phase (i.e. the input text is mapped to a list of words). Then, we can ‘reduce’ this data into a coherent word count that holds for the entire text set. We do this by accumulating the count of each word in each chunk using our reduce function.

Take a look at `map_reducer.py` and `word_count.py` to see the example we’ve constructed for you. Notice that the `map` stage is being run on a multiprocess pool. This is functionally analogous to a cloud computing application, the difference being in the cloud, this work would be distributed amongst multiple nodes, whereas in our toy MapReduce, all the processes run on a single machine.

Run `python word_count.py` to see our simple map/reduce example. You can adjust `NUM_WORKERS` in `map_reducer.py` to see how we make (fairly small) performance gains from parallelizing the work. (Hint: running `time python word_count.py` will give you a better idea of the runtime).

## Exercise: Bigram Count

Suppose now that instead of trying to count the individual words, we want to get counts of the occurrences word [bigrams](https://en.wikipedia.org/wiki/Bigram) - that is, pairs of words that are *adjacent* to each other in the text (Bigrams are **not** just all the pairs of the words in the text).

For example, if our line of text was `“cat dog sheep horse”`, we’d have the bigrams `(“cat”, “dog”)`, `(“dog, “sheep”)` and `(“sheep”, “horse”)`.

Construct a map function and reduce function that will accomplish this goal.

**Note:** For the purposes of this exercise, we’ll only consider bigrams that occur on the same line. So, you don’t need to worry about pairs that occur between line breaks.

### Example:
Input: (stdin)
```
the dog in the tree
the cat in the hat
in summer the dog swam
```

Output: (stdout)
```
(the, dog): 2
(dog, in): 1
(in, the): 2
(the, tree): 1
(the, cat): 1
(cat, in): 1
(the, hat): 1
(in, summer): 1
(summer, the): 1
(dog, swam): 1
```

Note that the order of the output is not important in this exercise.

## Exercise: Common Friends

Suppose we’re running a social network and we want a fast way to calculate a list of common friends for pairs of users in our site. This can be done with a map/reduce procedure.

You’ll be given input of a friend ‘graph’ that looks like this:

```
A|B
B|A,C,D
C|B,D
D|B,C,E
E|D
```
The graph can be visualized as
``` 
A-B - D-E
   \ /
    C
```
Read this as: A is friends with B, B is friends with A, C and D, and so on. Our desired output is as follows:

```
(A,C): [B]
(A,D): [B]
(B,C): [D]
(B,D): [C]
(B,E): [D]
(C,D): [B]
(C,E): [D]
```

Read this as: A and C have B in common as a friend, A and D have B in common as a friend, and B and C have D in common as a friend, and so on. None of the other relationships have common friends.
(For example, A and E have no common friends)

Note that each list of common friends should only be outputted once. (i.e. There should not be entries for `(A, C)` and `(C, A)`)

#### Suggestions:
Your mapper stage should take each line of the friend graph and produce a multiple key/value pairs keyed with a relationship, with value being immediately known common friends.
The reducer phase should take all of these relationships and output common friends for each pair. (Hint: Lookup set union)

**Note:** This problem is a bit challenging. Try your best to figure it out before asking for help. :)

## Submission

MP 1 is due on **Wednesday, September 13nd, 2017** at 11:55PM.

Please zip the files and upload it to [Moodle](learn.illinois.edu). Place all your source files into a single folder and zip it. When we unzip your files, we should be left with a single folder that contains your source files.

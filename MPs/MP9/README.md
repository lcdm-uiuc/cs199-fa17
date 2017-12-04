# MP 9: Introduction to NoSQL

## Introduction

This MP will introduce the Open Source NoSQL database called [MongoDB](https://github.com/mongodb/mongo).

MongoDB is a Document-Oriented NoSQL database. This allows applications to persist large amounts of unstructured data. MongoDB's "atomic unit" is a document -- analogous to record in a SQL database. MongoDB's equivalent of a "table" is a "collection".

### Resources

For this MP, you'll find the following Resources useful:

* [MongoDB Python Driver Documentation](https://api.mongodb.com/python/current/)
* This MongoDB article explaining common operations: https://docs.mongodb.com/manual/crud/
* Getting started with MongoDB using Python: https://docs.mongodb.com/getting-started/python/

## MP Activities

In this MP we'll revisit the Yelp dataset we used earlier in the course. This MP will have you interact with MongoDB by loading a portion of the Yelp dataset into MongoDB. Then, you'll run some basic queries.

### Problem 1 - Create and Populate the Collection

**Step 1:** Create a new collection called `businesses`.

**Step 2:** Add the Yelp Business data to the MongoDB collection you created. Persist all attributes in the original dataset. (*Hint:* Since MongoDB is schema-less, try to insert data into the collection without doing anything dependent on the data's structure)

**Step 3:** Return the number of inserted businesses.

### Problem 2 - Retrieving Data

Complete the `find_urbana_businesses` function so that it queries the `businesses` collection and returns all the business that have their `city` value as "Urbana" and `state` value as "IL".

Return these businesses as `(name, address)` tuples.

### Problem 3 - Updating Data

Now suppose that we want to update our database. We've decided that Yelp users underrate businesses on Green Street in Champaign and Urbana. To fix this, we decide to give an extra star to every business in Champaign and Urbana.

Complete the `add_stars_to_cu_businesses` so that every business in the collection that has a `city` value of "Urbana" or "Champaign" AND is has a `state` value of "IL" AND the word 'Green' is in it's `address` field (case insensitive) a new `stars` value that is one greater than its original value. Note that we'll stick with the conventions of our data and enforce that all businesses have `star` values `<=5`.

Return the number of updated businesses.

### Problem 4 - Deleting Data

Now suppose we have decided that we only care about business in Illinois. We decide that we're going to delete all businesses from our collection that do not have `state` being 'IL'.

Complete the function so that the only remaining businesses in the database are businesses in IL. Return the number of deleted businesses.

## Deliverables
**MP 9 is due on Wednesday, December 13nd, 2017 at 11:55PM.**

Please zip your source files for the following exercises and upload it to Moodle (learn.illinois.edu).

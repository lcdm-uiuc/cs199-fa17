import pymongo as pm
import getpass


# Part 1
def setup_business_collection(db, data):
    '''
    Creates a new collection using the name "businesses"
    and adds new documents `data` to our MongoDB collection.

    Parameters
    ----------
    db: A pymongo.database.Database instance.
    data: A list of unparsed JSON strings.

    Returns
    -------
    int: The number of inserted businesses
    '''
    pass


# Part 2
def find_urbana_businesses(db):
    '''
    Queries the MongoDB collection for businesses in Urbana, IL

    Parameters
    ----------
    db: A pymongo.database.Database instance.

    Returns
    -------
    A list of (name, address) tuples
    '''
    pass


# Part 3
def add_stars_to_green_street_businesses(db):
    '''
    Adds one star to any businesses on Green Street in Champaign/Urbana IL
    Returns the number of updated businesses

    Parameters
    ----------
    db: A pymongo.database.Database instance.

    Returns
    -------
    int: The number of updated businesses
    '''
    pass


# Part 4
def delete_non_il_businesses(db):
    '''
    Deletes any businesses in the MongoDB colleciton that are not in Illinois

    Parameters
    ----------
    db: A pymongo.database.Database instance.

    Returns
    -------
    int: The number of deleted businesses
    '''
    pass


if __name__ == '__main__':
    username = getpass.getuser()
    client = pm.MongoClient("mongodb://localhost:27017")

    # We will delete our database if it exists before recreating
    if username in client.database_names():
        client.drop_database(username)

    db = client[username]

    # Load the data in from disk to MongoDB
    with open('/data/business.json') as f:
        num_businesses = setup_business_collection(db, f.readlines())

    print("Inserted {} businesses".format(num_businesses))

    # Query the table for urbana businesses
    print("Some Urbana Businesses:")
    print('\n'.join(
        ['{}\t{}'.format(*result) for result in find_urbana_businesses(db)[:10]]
    ))

    green_street = add_stars_to_green_street_businesses(db)
    print("Green Street Businesses Updated: {}".format(green_street))

    deleted_businesses = delete_non_il_businesses(db)
    print("Deleted non-Illinois businesses: {}".format(deleted_businesses))

    print("There are {} CU businesses remaining in the DB".format(db['businesses'].count()))

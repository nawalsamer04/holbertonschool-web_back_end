#!/usr/bin/env python3
"""
Insert a new document in a MongoDB collection.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document in the collection based on kwargs.
    Return the new document id.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id

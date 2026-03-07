#!/usr/bin/env python3
"""
Update topics of school documents based on name.
"""


def update_topics(mongo_collection, name, topics):
    """
    Change all topics of school documents based on the given name.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )

#!/usr/bin/env python3
"""
Returns all students sorted by average score.
"""


def top_students(mongo_collection):
    """
    Return all students sorted by average score.
    The average score is stored in key 'averageScore'.
    """
    students = list(mongo_collection.find())

    for student in students:
        topics = student.get("topics", [])
        if topics:
            avg = sum(topic.get("score", 0) for topic in topics) / len(topics)
        else:
            avg = 0
        student["averageScore"] = avg

    return sorted(students, key=lambda x: x["averageScore"], reverse=True)

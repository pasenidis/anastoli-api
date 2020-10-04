import re

def research(school, total):
    """Search algorithm"""
    return contains(total, lambda x: school.lower() in x['name'].lower())

def contains(list, filter):
    for x in list:
        if filter(x):
            return x
    return False
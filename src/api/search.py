import re

def research(school, total):
    """Search based on regular expressions"""
    match = None
    for _ in total:
        if _['name'] == school or _['name'].lower() == school.lower() or _['name'].upper() == school.upper():
            match = _
            break
        else:
            continue
    return match
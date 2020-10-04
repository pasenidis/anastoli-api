import re

def research(school, total):
    """Search based on regular expressions"""
    for _ in total:
        regex = fr"^{school}"
        if re.match(regex, _['name'], flags=re.IGNORECASE):
            return _
            break
        else:
            continue
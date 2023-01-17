

def accum(s):
    return '-'.join(char.upper() + char.lower() * i for i, char in enumerate(s))
"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    list = []
    for k in items:
        if isinstance(k,int):
            list.append(str(k))
        else:
            list.append(k)           
    for i in list:
        count = 0
        for j in list:
            if i==j:
                count+=1
        frequencies[i] = count
    return frequencies

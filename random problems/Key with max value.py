""" 
Tip : To check if type of value of a key is not a list then make it a list:

if not isinstance(dict[key], list):
    dict[key] = [dict[key]]

"""

"""
Q: Find the key with maximum value.
"""

def max_key(dict):
    max = 0
    for key in dict.keys():
        if max < dict[key]:
            max = dict[key]
            max_key = key
    return max_key


dict_keys = input().split()
dict_values = list(map(int, input().split()))

dict = { k : v 
        for k, v in zip(dict_keys, dict_values)}
        #zip() function returns an iterator of tuples in which similar index of multiple containers are mapped together.

print(max_key(dict))
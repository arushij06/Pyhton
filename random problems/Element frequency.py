"""
Given an array, write a function to print frequency of each word in the sentence.

Input:                  Output:
geeks for geeks         geeks: 2
                        for: 1
"""


def printWordFrequency(sentence):
    dict = {}
    max_value_key = 0
    for word in sentence:
        previous_count_of_word = dict.get(word, 0)
        dict[word] = previous_count_of_word + 1
        if dict.get(max_value_key, -1) < dict[word]:
            max_value_key = word
    print(dict, max_value_key)

sentence = list(input().split())
printWordFrequency(sentence)

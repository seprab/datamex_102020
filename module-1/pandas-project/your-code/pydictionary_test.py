from PyDictionary import PyDictionary

dictionary=PyDictionary("swimming")
'''There can be any number of words in the Instance'''

'''This print the meanings of all the words'''
print(dictionary.printMeanings())

'''This will return meanings as dictionaries'''
print(dictionary.getMeanings())
print(dictionary.getSynonyms())
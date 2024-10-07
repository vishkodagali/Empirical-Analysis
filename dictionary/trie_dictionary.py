from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency
import time


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Trie-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------


# Class representing a node in the Trie
class TrieNode:

    def __init__(self, letter=None, frequency=None, is_last=False):
        self.letter = letter  # Letter stored at this node
        self.frequency = frequency  # frequency of the word if this letter is the end of a word
        self.is_last = is_last  # True if this letter is the end of a word
        self.children: dict[str, TrieNode] = {}  # a hashtable containing children nodes, where the key is letter and
        # the value is child


class TrieDictionary(BaseDictionary):

    def __init__(self):
        # TO BE IMPLEMENTED
        self.rootNode = TrieNode()  # Initializing the root node of trie

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # TO BE IMPLEMENTED
        # Iterating through the list of WordFrequency items and adding each item to the trie dictionary
        for item in words_frequencies:
            self.add_word_frequency(item)  # adding the WordFrequency items to the trie by calling the function
            # add_word_frequency

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # TO BE IMPLEMENTED
        start = time.time_ns()
        # print(word)
        iterator = self.rootNode  # Initialize an iterator at the node of the trie
        # Start iterating through each letter in the word parameter
        for a_Letter in word:
            # Checking if the iterated letter exists in the child of the node
            if a_Letter in iterator.children:
                iterator = iterator.children[a_Letter]  # moving the iterator to the child node
            else:
                return 0  # if the letter is not found then return 0
        # check if the iterator node indicates the end of a word
        # end = time.time_ns()
        # print(end - start)
        if iterator.is_last:
            return iterator.frequency  # returning the frequency of the word
        return 0  # the whole word is not found in the trie so return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        # TO BE IMPLEMENTED
        # Initializing the iterator to the root node
        iterator = self.rootNode
        # Iterate through each letter in the word of the pass parameter WordFrequency
        for a_Letter in word_frequency.word:
            # if the iterated letter is not found the children node
            if a_Letter not in iterator.children:
                iterator.children[a_Letter] = TrieNode(a_Letter)  # adding a new TrieNode object for the current letter
            iterator = iterator.children[a_Letter]  # moving the iterator to the child node
        # check if the iterator node is the end of the word
        if iterator.is_last:
            return False  # word already exists in the dictionary, return false
        iterator.is_last = True  # set the end of the word
        iterator.frequency = word_frequency.frequency  # set the words frequency
        return True  # returning true if the word and frequency is added to the dictionary

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        # print(word)
        # start = time.time_ns()
        iterator = self.rootNode  # Initialize iterator to the root node of the trie
        temp_nodes = []  # creating a temporary list to store parent-child
        # Iterate through each letter in the word parameter
        for a_Letter in word:
            # if the iterated letter is found in the child
            if a_Letter in iterator.children:
                temp_nodes.append((iterator, a_Letter))  # store the link of the parent-child
                iterator = iterator.children[a_Letter]  # move iterator to child node
            else:
                return False  # returning false if the word is not found in the trie
        # Word not found in the trie
        if not iterator.is_last:
            return False  # returning false if the word is not found in the trie

        iterator.is_last = False  # setting the end of the word as false
        iterator.frequency = None  # setting the frequency to none for that word to remove

        # check if any nodes are part of other words
        for parent, a_Letter in reversed(temp_nodes):
            if iterator.is_last or iterator.children:
                break
            del parent.children[a_Letter]
            iterator = parent
        # end = time.time_ns()
        # print(end-start)
        return True  # if the word is removed from the trie then return true

    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        iterator = self.rootNode  # Initialize iterator to the root node of the trie
        # Iterate through each letter in the word parameter
        for a_Letter in word:
            if a_Letter in iterator.children:
                iterator = iterator.children[a_Letter]  # Move the iterator to the child node
            else:
                return []  # if no words in the dictionary match the word parameters
        res = []  # List to store frequent words that match the prefix
        self.get_frequent_item(iterator, word, res)  # calling the function to get the frequent words
        res.sort(key=lambda item: item.frequency, reverse=True)  # Sort the result list by frequency in descending order
        return res[:3]  # Return top most 3 frequent words

    def get_frequent_item(self, temp_node: TrieNode, word: str, res: list):
        if temp_node.is_last:
            res.append(WordFrequency(word, temp_node.frequency))  # adding the frequent word to the result list
        # Recursion to iterate child nodes to continue forming words
        for a_letter, item in temp_node.children.items():
            self.get_frequent_item(item, word + a_letter, res)

import time
from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency


class ListNode:
    '''
    Define a node in the linked list
    '''

    def __init__(self, word_frequency: WordFrequency):
        # Store the WordFrequency object
        self.word_frequency = word_frequency
        # Declaring the next pointer to None
        self.next = None


# ------------------------------------------------------------------------
# This class  is required TO BE IMPLEMENTED
# Linked-List-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------
class LinkedListDictionary(BaseDictionary):

    def __init__(self):
        # TO BE IMPLEMENTED
        self.head = None  # Initializing the head of the linked list to None

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # TO BE IMPLEMENTED
        # Iterating through the list of WordFrequency items
        for item in words_frequencies:
            self.add_word_frequency(item)  # Add the WordFrequency item to the dictionary by calling function
            # add_word_frequency

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # TO BE IMPLEMENTED
        iterator = self.head  # Initialize an iterator to iterate through the linked list
        # Iterate through the liked list
        while iterator:
            # Check if the word, if it matches the iterated node
            if iterator.word_frequency.word == word:
                # if the word is found and has positive frequency then return the frequency
                if iterator.word_frequency.frequency > 0:
                    # print(iterator.word_frequency.word)
                    return iterator.word_frequency.frequency
            iterator = iterator.next  # move the iterator to the next node
        return 0  # if the wor is not found or the frequency is not greater than 0 then return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        # TO BE IMPLEMENTED
        node = ListNode(word_frequency)  # create a new node with the parameter WordFrequency
        # if the linked list in empty, set the new node as the head and return true
        if self.head is None:
            self.head = node
            return True
        # Iterate through the linked list to check for existing words
        iterator = self.head
        while iterator.next:
            # check if the word in the current node matches the iterated word_frequency's word
            if iterator.word_frequency.word == word_frequency.word:
                return False  # return false if the word already exist in the dictionary
            iterator = iterator.next  # moving the iterator to the next node
        # checking the last nodes word if any duplicates
        if iterator.word_frequency.word == word_frequency.word:
            return False  # return false if there is a duplicate found
        iterator.next = node  # adding the new nod to the end of the linked list
        return True  # return true if the new word_frequency is added to the linked list

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        # TO BE IMPLEMENTED
        # checking if the linked list is empty
        if self.head is None:
            return False  # if the linked list is empty the return false
        # checking if the word to be removed is in the head node of the linked list
        if self.head.word_frequency.word == word:
            self.head = self.head.next  # update the head to the next node
            return True  # return true if the word is matched with the head
        iterator = self.head  # Iterate through the linked list to find and remove the specified word
        while iterator.next:
            # If the word match then point the next of the iterated node to the next of next
            if iterator.next.word_frequency.word == word:
                # pointing the iterated node to the next of next node to remove the desired node
                iterator.next = iterator.next.next
                return True  # returning true if the node is removed
            iterator = iterator.next  # moving the iterator to the next node
        return False  # return false if the word is not found

    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        # TO BE IMPLEMENTED
        auto_complete = []  # create a list to store autocomplete to store the results
        iterator = self.head  # Initialize an iterator at the beginning of the linked list
        # Iterate through the linked list
        while iterator:
            #  check if the word is in the current node start with the input word parameter
            if iterator.word_frequency.word.startswith(word):
                auto_complete.append(iterator.word_frequency)  # Add the WordFrequency to the list of auto complete
            iterator = iterator.next  # move the iterator to the next node
        auto_complete.sort(key=lambda item: item.frequency,
                           reverse=True)  # Sort the list auto_complete by frequency in descending order
        return auto_complete[:3]  # return the top 3 most word from the auto_complete list

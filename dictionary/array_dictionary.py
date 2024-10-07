from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary
import time

# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Array-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------


class ArrayDictionary(BaseDictionary):

    def __init__(self):
        # TO BE IMPLEMENTED
        self.new_dictionary = []  # create a list to store the entries

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # TO BE IMPLEMENTED
        words_frequencies.sort(key=lambda lambda_item: lambda_item.word)  # Sorting the list of WordFrequency objects
        # using words by lambda function
        self.new_dictionary = words_frequencies  # Assignment operation to store the list of WordFrequency objects to
        # the new_dictionary

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        start_time = time.time_ns()
        # TO BE IMPLEMENTED
        # Iterating through the new_dictionary to find word and its frequency
        for item in self.new_dictionary:
            #  if the word is found and matches then goes to the next if loop
            if item.word == word:
                # if the word has a positive frequency then the if loop returns the words frequency
                if item.frequency > 0:
                    # end_time = time.time_ns()
                    # time_taken = end_time - start_time
                    # print(time_taken)
                    return item.frequency
        # if the word is not found or frequency is 0 then return 0
        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
          add a word and its frequency to the dictionary
          @param word_frequency: (word, frequency) to be added
          :return: True whether succeeded, False when word is already in the dictionary
        """
        # TO BE IMPLEMENTED
        # Iterating through the new_dictionary to check whether the word exists
        for item in self.new_dictionary:
            # if the input parameter matches the word then return False
            if item.word == word_frequency.word:
                return False
        self.new_dictionary.append(word_frequency)  # add the new word and frequency to the new_dictionary
        self.new_dictionary.sort(key=lambda lambda_item: lambda_item.word) # sort the array as there is a new change
        return True  # return true if the new word was added to the new_dictionary

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        # find the position of 'word' in the list, if exists, will be at idx-1
        # TO BE IMPLEMENTED
        # Iterating through the new_dictionary to find the word to be removed
        # start_time = time.time_ns()
        for item in self.new_dictionary:
            # if the word is found then the if loop executes
            if item.word == word:
                # print(item.word)
                self.new_dictionary.remove(item)  # use the remove function to remove the item from the dictionary
                self.new_dictionary.sort(
                    key=lambda lambda_item: lambda_item.word)  # sort the dictionary as there is change, using lambda
                # end_time = time.time_ns()
                # time_taken = end_time - start_time
                # print(time_taken)
                return True  # returning true if the word is successfully removed from the dictionary
        return False  # if the word not found then return false

    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'prefix_word' as a prefix
        @param prefix_word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'prefix_word'
        """
        #  create a list to store the results of the auto completed words
        auto_complete = []
        # Iterate through the new_dictionary to find the words
        for item in self.new_dictionary:
            # if the iterated item starts with the input parameter prefix
            if item.word.startswith(prefix_word):
                auto_complete.append(item)  # append the words that starts with the same prefix parameter
        auto_complete.sort(
            key=lambda lambda_item: lambda_item.frequency, reverse=True)  # sort the list
        # auto_complete by frequency in reverse order to get the higher frequency for auto complete
        return auto_complete[:3]  # Return the top 3 most words from the list

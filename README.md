# Empirical Analysis of Dictionary Data Structures

This project involves the implementation and empirical analysis of different data structures for a dictionary application. The primary focus is on three data structures: Array (Python list), Linked List, and Trie. The analysis evaluates the performance of common dictionary operations such as Add, Search, Delete, and Autocomplete, considering different dataset sizes.

## Table of Contents
- [Objectives](#objectives)
- [Project Structure](#project-structure)
- [Data Structures Implemented](#data-structures-implemented)
- [Operations](#operations)
- [Data Generation](#data-generation)
- [Experimental Setup](#experimental-setup)
- [Analysis](#analysis)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [How to Run](#how-to-run)
- [Results](#results)
- [References](#references)

## Objectives
- Implement a dictionary using three different data structures: Array, Linked List, and Trie.
- Compare the performance of these data structures under various scenarios and input sizes.
- Conduct empirical analysis and provide insights on their time complexities.

## Project Structure
- **`array_dictionary.py`**: Implements the dictionary using Python's list data structure.
- **`linkedlist_dictionary.py`**: Implements the dictionary using a singly linked list.
- **`trie_dictionary.py`**: Implements the dictionary using the Trie data structure.
- **`dictionary_file_based.py`**: The main module for testing and evaluating the dictionary implementations.
- **`test_script.py`**: Automated test script for evaluating performance and correctness.
- **`sampleData.txt`**: Provides sample datasets of words and their frequencies.
- **`report/`**: Contains the empirical analysis report (PDF format) detailing the experiment and findings.

## Data Structures Implemented
1. **Array-Based Dictionary**: Utilizes Python's dynamic list, storing words and their frequencies in an alphabetically sorted manner.
2. **Linked List-Based Dictionary**: Uses a singly linked list to store words and frequencies as nodes. The words are not stored in a sorted order.
3. **Trie-Based Dictionary**: Implements a trie to store (word, frequency) pairs. Allows efficient search and auto-completion operations.

## Operations
- **Add**: Adds a word and its frequency to the dictionary.
- **Search**: Searches for a word and returns its frequency.
- **Delete**: Deletes a word from the dictionary.
- **Autocomplete**: Returns up to three words with the given prefix, sorted by frequency.

## Data Generation
- The dataset used in this project is based on the file `sampleData200k.txt`, containing 200,000 word-frequency pairs.
- Datasets of varying sizes (500 to 175,000 records) were generated for empirical analysis.

## Experimental Setup
- Time measurements were taken using Python's `time.time_ns()` for high precision.
- Each operation (Add, Search, Delete, Autocomplete) was tested on datasets of different sizes.
- Each test was repeated 10 times, and the average time was recorded to ensure accuracy.

## Analysis
- The performance of each data structure was analyzed using empirical data and compared against theoretical time complexities.
- Detailed analysis and comparisons are provided in the accompanying report.

## Usage
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/vishkodagali/Empirical-Analysis.git
    cd Empirical-Analysis
    ```
2. **Run the Main Module**:
    ```bash
    python3 dictionary_file_based.py <approach> <data filename> <command filename> <output filename>
    ```
    - `<approach>`: One of `array`, `linkedlist`, `trie`.
    - `<data filename>`: File containing the initial set of words and frequencies.
    - `<command filename>`: File with the commands/operations.
    - `<output filename>`: File to store the output.

3. **Run the Automated Tests**:
    ```bash
    python3 test_script.py
    ```

## Dependencies
- Python 3.10 or later
- No external libraries are required.

## How to Run
1. Ensure Python 3.10+ is installed.
2. Run the `dictionary_file_based.py` module as described in the Usage section.
3. For evaluation, run the `test_script.py` to check the implementation against provided datasets.

## Results
- Empirical analysis results, graphs, and conclusions are documented in the report found in the `report/` directory.

## References
- The project references various resources for implementing and analyzing the data structures. Detailed references can be found in the analysis report.

---

For more details, please refer to the `report/Empirical_Analysis_Report.pdf` in the repository.

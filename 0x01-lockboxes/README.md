# 0x01. Lockboxes

## 📚 Introduction
This Python script provides a solution to the lock boxes puzzle. The lock boxes
puzzle involves a set of sequentially numbered boxes, where each box may
contain keys to other boxes. The goal is to determine if it's possible to
unlock all boxes, starting from an initially unlocked box. 🧩

## Concepts Needed:
- **Lists and List Manipulation:**
    - Understanding how to work with lists, including accessing elements,
iterating over lists, and modifying lists dynamically.
    - [Python Lists (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html)

- **Graph Theory Basics:**
    - Although not explicitly required, knowledge of graph theory (especially
concepts related to traversal algorithms like Depth-First Search or
Breadth-First Search) can be very helpful in solving this problem, as the boxes
and keys can be thought of as nodes and edges in a graph.
    - [Graph Theory (Khan Academy)](https://www.khanacademy.org/computing/computer-science/algorithms)

- **Algorithmic Complexity:**
    - Understanding the time and space complexity of your solution is
important, as it can help in writing more efficient algorithms.
    - [Big O Notation (GeeksforGeeks)](https://www.geeksforgeeks.org/analysis-algorithms-big-o-analysis/)

- **Recursion:**
    - Some solutions might require a recursive approach to traverse through the
boxes and keys.
    - [Recursion in Python (Real Python)](https://realpython.com/python-thinking-recursively/)

- **Queue and Stack:**
    - Knowing how to use queues and stacks is crucial if implementing a
breadth-first search (BFS) or depth-first search (DFS) algorithm to traverse
through the keys and boxes.
    - [Python Queue and Stack (GeeksforGeeks)](https://www.geeksforgeeks.org/queue-in-python/)

- **Set Operations:**
    - Understanding how to use sets for keeping track of visited boxes and
available keys can optimize the search process.
    - [Python Sets (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html)

By reviewing these concepts and utilizing these resources, you will be
well-equipped to develop an efficient solution for this project, applying both
your algorithmic thinking and Python programming skills.

## Additional Resources
- [Mock Technical Interview](https://www.mockinterview.co/)

# Requirements
## General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3
(version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should be documented
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable

# Tasks
## 0. Lockboxes (mandatory)

You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

- **Prototype:** `def canUnlockAll(boxes)`
- `boxes` is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
- There can be keys that do not have boxes
- The first box `boxes[0]` is unlocked
- Return `True` if all boxes can be opened, else return `False`

## File Structure
- **lock_boxes_solver.py**: This Python script contains the implementation of
the lock boxes puzzle solver.
- **README.md**: This markdown file provides an overview of the script and its
functionality.

## Functions

### `look_next_opened_box(opened_boxes)` 🔒
This function looks for the next opened box in a dictionary containing
information about already opened boxes.

**Parameters:**
- `opened_boxes` (dict): A dictionary containing information about already
opened boxes.

**Returns:**
- A list of keys contained in the opened box.

### `canUnlockAll(boxes)` 📦🔓
This function checks if all boxes can be opened.

**Parameters:**
- `boxes` (list): A list containing all the boxes with the keys.

**Returns:**
- True if all boxes can be opened, otherwise False. 🎉

### `main()` 🚀
This function serves as the entry point for the script.

## Implementation Details

1. **Initialization**: The `canUnlockAll` function initializes an empty
dictionary `aux` to keep track of opened boxes and their keys.

2. **Breadth-First Search (BFS)**: The function performs a BFS traversal
starting from the initially unlocked box (box 0). It iteratively explores all reachable boxes, adding their keys to `aux`.

3. **Box Status Tracking**: The status of each box (opened or checked) is
tracked using a dictionary with keys representing box indices and values
containing status information.

4. **Loop Termination**: The BFS loop continues until all boxes are checked or
until it's determined that all boxes cannot be opened.

5. **Return Value**: The function returns True if all boxes can be opened,
otherwise False.

## Usage
To use the lock boxes puzzle solver, simply call the `canUnlockAll` function
with a list of boxes as input.

Example usage:
```
canUnlockAll([[1], [2], [3], [0]])
```



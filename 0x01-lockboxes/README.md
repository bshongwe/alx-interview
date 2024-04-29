# 0x01. Lockboxes

## Introduction
This Python script provides a solution to the lock boxes puzzle. The lock boxes
puzzle involves a set of sequentially numbered boxes, where each box may
contain keys to other boxes. The goal is to determine if it's possible to
unlock all boxes, starting from an initially unlocked box.

## File Structure
- **lock_boxes_solver.py**: This Python script contains the implementation of
the lock boxes puzzle solver.
- **README.md**: This markdown file provides an overview of the script and its
functionality.

## Functions

### `look_next_opened_box(opened_boxes)`
This function looks for the next opened box in a dictionary containing
information about already opened boxes.

**Parameters:**
- `opened_boxes` (dict): A dictionary containing information about already
opened boxes.

**Returns:**
- A list of keys contained in the opened box.

### `canUnlockAll(boxes)`
This function checks if all boxes can be opened.

**Parameters:**
- `boxes` (list): A list containing all the boxes with the keys.

**Returns:**
- True if all boxes can be opened, otherwise False.

### `main()`
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
```python
canUnlockAll([[1], [2], [3], [0]])



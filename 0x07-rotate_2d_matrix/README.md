# 🔄 0x07. Rotate 2D Matrix 🌀
`Algorithm` `Python`
<br></br>
## Overview
In the **Rotate 2D Matrix** project, your task is to implement an in-place algorithm to rotate an n x n 2D matrix by 90 degrees clockwise. This challenge requires a good understanding of matrix manipulation and in-place operations in Python.
<br></br>
## Key Concepts
### Matrix Representation in Python 🧩
- **Understanding:** How 2D matrices are represented using lists of lists in Python.
- **Operations:** Accessing and modifying elements in a 2D matrix.

### In-place Operations 💾
- **Concept:** Performing operations on data without creating a copy of the data structure.
- **Efficiency:** Minimizing space complexity by modifying the matrix in place.

### Matrix Transposition 🔄
- **Understanding:** The concept of transposing a matrix (swapping rows and columns).
- **Implementation:** Implementing matrix transposition as a step in the rotation process.

### Reversing Rows in a Matrix ↔️
- **Manipulation:** Reversing the order of rows as part of the rotation process.

### Nested Loops 🔁
- **Usage:** Using nested loops to iterate through 2D data structures like matrices.
- **Modification:** Modifying elements within nested loops to achieve the desired rotation.
<br></br>
## Resources 📚
### Python Official Documentation
- **Data Structures:** [List Comprehensions and Nested List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- **Lists:** [More on Lists](https://docs.python.org/3/tutorial/datastructures.html)

### GeeksforGeeks Articles
- **Rotation:** [Inplace Rotate Square Matrix by 90 Degrees](https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/)
- **Transpose:** [Transpose a Matrix in Single Line in Python](https://www.geeksforgeeks.org/transpose-matrix-single-line-python/)

### TutorialsPoint
- **Basics:** [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm)

By understanding these concepts and utilizing the provided resources, you will be able to approach the problem methodically. First, transpose the matrix, then reverse each row to achieve a 90-degree clockwise rotation. This project tests your ability to manipulate 2D matrices and challenges you to optimize your solution to operate in-place, thus improving your problem-solving and algorithmic thinking skills in Python.

## Additional Resources

- **Mock Technical Interview**
<br></br>

## Requirements 📝
### General
- **Editors:** `vi`, `vim`, `emacs`
- **Environment:** Ubuntu 20.04 LTS using Python 3 (version 3.8.10)
- **File Endings:** All files must end with a new line.
- **First Line:** The first line of all files should be `#!/usr/bin/python3`.
- **README.md:** A mandatory README file at the root of the project.
- **Coding Style:** Your code should use the pycodestyle style (version 2.8.0).
- **Imports:** You are not allowed to import any module.
- **Documentation:** All modules and functions must be documented.
- **Executables:** All files must be executable.
<br></br>

## Tasks
### 0. Rotate 2D Matrix 🔄
- **Objective:** Rotate a given n x n 2D matrix 90 degrees clockwise.
- **Prototype:**
  ```python
  def rotate_2d_matrix(matrix):
  ```
- **Requirements:**
  - Do not return anything. The matrix must be edited in-place.
  - Assume the matrix will have 2 dimensions and will not be empty.

**Example:**
```python
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    rotate_2d_matrix(matrix)
    print(matrix)
```

**Output:**
```bash
$ ./main_0.py
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

## Repository

- **GitHub Repository:** [alx-interview](https://github.com/bshongwe/alx-interview)
- **Directory:** `0x07-rotate_2d_matrix`
- **File:** `0-rotate_2d_matrix.py`

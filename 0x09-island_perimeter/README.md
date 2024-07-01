# 0x09. Island Perimeter 🏝️

## Project Description 📜
This project involves solving the problem of calculating the perimeter of a single island in a grid. The grid is represented by a 2D array of integers where:
- `0` represents water.
- `1` represents land.
- Each cell is square, with a side length of 1.
- Cells are connected horizontally and vertically (not diagonally).
- The grid is rectangular, with dimensions not exceeding 100x100.
- The grid is completely surrounded by water.
- There is only one island or no island at all (no lakes).
<br></br>

To achieve this, the solution requires knowledge of:
- 2D Arrays (Matrices) 🔄
  - Accessing and iterating over elements in a 2D array.
  - Navigating through adjacent cells (horizontally and vertically).
<br></br>

- Conditional Logic 🛠️
  - Applying conditions to determine whether a cell contributes to the perimeter of the island.
<br></br>

- Counting Techniques 📊
  - Developing a method to count the edges that contribute to the island’s perimeter.
<br></br>

- Problem-Solving Strategies 💡
  - Breaking down the problem into smaller tasks, such as identifying land cells and calculating their contribution to the perimeter.
<br></br>

- Python Programming 🐍
  - Using nested loops for iterating over grid cells.
  - Using conditional statements to check the status of adjacent cells.
<br></br>

## Requirements 📋
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using Python3 (version 3.4.3).
- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/python3`.
- A `README.md` file, at the root of the folder of the project, is mandatory.
- Your code should use the PEP 8 style (version 1.7).
- You are not allowed to import any module.
- All modules and functions must be documented.
- All your files must be executable.
<br></br>

## Tasks ✅
### 0. Island Perimeter 🏝️
Create a function `def island_perimeter(grid):` that returns the perimeter of
the island described in `grid`:

- `grid` is a list of list of integers:
  - `0` represents water.
  - `1` represents land.
  - Each cell is square, with a side length of 1.
  - Cells are connected horizontally/vertically (not diagonally).
  - `grid` is rectangular, with its width and height not exceeding 100.
- The grid is completely surrounded by water.
- There is only one island (or nothing).
- The island doesn’t have “lakes” (water inside that isn’t connected to the
water surrounding the island).

### Example 🌊

```python
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))  # Output should be 12
```
<br></br>

## Additional Resources 📚

- [Python Official Documentation: Nested Lists](https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions)
- [GeeksforGeeks: Python Multi-dimensional Arrays](https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/)
- [TutorialsPoint: Python Lists](https://www.tutorialspoint.com/python/python_lists.htm)
- [YouTube Tutorials on Python 2D arrays and lists](https://www.youtube.com/watch?feature=shared&v=aNzepGawwCI)

---
By understanding these concepts and utilizing the provided resources, you will be equipped to approach the problem methodically. This project not only tests your algorithmic thinking but also reinforces your ability to manipulate data structures and apply logical reasoning to solve problems.

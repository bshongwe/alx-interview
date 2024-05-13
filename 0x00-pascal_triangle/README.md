# Pascal's Triangle in Python 📚
## 0x00. Pascal's Triangle 📊
🌰 `Algorithm` `Python`
<br></br>

### Resources ℹ️
-  [What is Pascal’s triangle](https://www.cuemath.com/algebra/pascals-triangle/)
-  [Pascal’s Triangle - Numberphile](https://www.youtube.com/watch?feature=shared&v=0iMtlus-afo)
-  [What are Python Algorithms](https://builtin.com/data-science/python-algorithms)
<br></br>

### Additional Resources 📚
-  [Mock Technical Interview](https://www.youtube.com/watch?feature=shared&v=1qw5ITr3k9E)
<br></br>

### Must Know 🧠
To successfully complete this project, you should revise the following Python concepts:
**Lists and List Comprehensions:**
  - Understand how to create, access, modify, and iterate over lists.
  -  Utilize list comprehensions for more concise and readable code, especially for generating rows of Pascal’s Triangle.
<br></br>

**Functions:**
  -  Know how to define and call functions.
  - Pass parameters and return values, particularly how to return a list of lists representing Pascal’s Triangle.
<br></br>

**Loops:**
  - Use for and while loops to iterate through sequences.
  - Nested loops may be necessary for generating each row and calculating the values of Pascal’s Triangle.
<br></br>

**Conditional Statements:**
  - Apply if, elif, and else conditions to implement logic based on the position within Pascal’s Triangle (e.g., the edges of the triangle always being 1).
<br></br>

**Recursion (Optional):**
  - While not strictly necessary, understanding recursion can provide an alternative approach to generating Pascal’s Triangle.
  - Recognize base cases and recursive cases for a function that generates the triangle’s rows.
<br></br>

**Arithmetic Operations:**
  - Perform addition, a fundamental operation for calculating each element of Pascal’s Triangle as the sum of the two elements directly above it.
<br></br>

**Indexing and Slicing:**
  - Access elements and slices of lists, crucial for identifying and summing the correct elements when constructing each row of the triangle.
<br></br>

**Memory Management:**
  - Be mindful of how lists are stored and copied, especially when creating new rows based on the values of the previous row.
<br></br>

**Error and Exception Handling (Optional):**
  - Use try-except blocks as needed to handle potential errors, such as invalid input types or values.
<br></br>

**Efficiency and Optimization:**
  - Consider the time and space complexity of different approaches to generating Pascal’s Triangle.
  - Evaluate and apply optimizations to improve the performance of the solution.
<br></br>

By revisiting these concepts, you will be well-prepared to tackle the challenges of implementing Pascal’s Triangle in Python, applying both your mathematical understanding and programming skills to develop an efficient and effective solution.

## Tasks ✅

### 0. Pascal's Triangle
**Mandatory**</br>
Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of n:
- Returns an empty list if n <= 0
- You can assume n will be always an integer

**0-main.py**
```python
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
```
<br></br>

## Repo Details 📁
- **GitHub repository:** alx-interview
- **Directory:** 0x00-pascal_triangle
- **File:** 0-pascal_triangle.py
- **Test File:** 0-main.py


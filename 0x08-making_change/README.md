# 0x08. Making Change 💰

## Project Overview 📝

This project, "0. Change comes from within," tackles a classic problem in the
domain of dynamic programming and greedy algorithms: the coin change problem.
The goal is to determine the minimum number of coins required to make up a
given total amount, given a list of coin denominations. This project will
challenge you to apply your understanding of algorithms to devise a solution
that is both correct and efficient.

## Key Concepts 📚

### Greedy Algorithms 🤖
- **Understanding Greedy Algorithms**: Learn how greedy algorithms make locally optimal choices to find a global optimum.
- **Limitations of Greedy Algorithms**: Recognize when greedy algorithms may not provide the optimal solution.

### Dynamic Programming 🧩
- **Principles of Dynamic Programming**: Use dynamic programming to solve optimization problems by breaking them down into simpler subproblems.
- **Overlapping Subproblems and Optimal Substructure**: Understand these concepts in the context of the coin change problem.

### Algorithmic Complexity ⏱️
- **Time and Space Complexity**: Analyze the efficiency of your algorithms.
- **Striving for Lower Complexity**: Aim to reduce the runtime and space requirements of your solutions.

### Problem-Solving Strategies 🛠️
- **Breaking Down the Problem**: Divide the coin change problem into smaller, manageable subproblems.
- **Iterative vs Recursive Approaches**: Compare different approaches to dynamic programming.

### Python Programming 🐍
- **List Manipulation and Comprehensions**: Work efficiently with Python lists.
- **Efficient Looping and Conditional Statements**: Implement functions using optimized loops and conditionals.

## Resources 📖

- **Python Official Documentation**: More Control Flow Tools (for loops, if statements)
- **GeeksforGeeks Articles**:
  - [Coin Change | DP-7](https://www.geeksforgeeks.org/coin-change-dp-7/)
  - [Greedy Algorithm to find Minimum number of Coins](https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/)
- **YouTube Tutorials**:
  - [Dynamic Programming - Coin Change Problem](https://www.youtube.com/watch?v=1R0_7HqNaW0)

By thoroughly understanding these concepts and utilizing the provided
resources, you will be well-prepared to tackle the coin change problem. You
will need to decide whether a greedy algorithm suffices for your particular set
of coin denominations or if a more comprehensive dynamic programming approach
is necessary to ensure correctness and efficiency. This project not only tests
algorithmic skills but also reinforces the importance of choosing the right
strategy based on problem constraints.

## Additional Resources 🎓

- Mock Technical Interview

## Requirements ✅

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable

## Tasks 📝

### 0. Change comes from within

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

#### Prototype
```python
def makeChange(coins, total)
```

#### Return
- Fewest number of coins needed to meet `total`
  - If `total` is 0 or less, return 0
  - If `total` cannot be met by any number of coins you have, return -1

#### Parameters
- `coins` is a list of the values of the coins in your possession
- The value of a coin will always be an integer greater than 0
- You can assume you have an infinite number of each denomination of coin in the list

#### Example Usage
```python
carrie@ubuntu:~/0x08-making_change$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))
print(makeChange([1256, 54, 48, 16, 102], 1453))

carrie@ubuntu:~/0x08-making_change$ ./0-main.py
7
-1
carrie@ubuntu:~/0x08-making_change$
```

## Repository 📂
```
- **GitHub Repository**: `alx-interview`
- **Directory**: `0x08-making_change`
- **File**: `0-making_change.py`
```

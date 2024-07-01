# 🎲 Project: 0x0A. Prime Game
`Algorithm` `Python`
<br></br>

## Overview
For this project, you will need to leverage your understanding of prime numbers, game theory, and algorithm optimization to solve a competitive game scenario. The challenge involves determining the winner of a game based on the strategic removal of prime numbers and their multiples from a set of consecutive integers.
<br></br>
<br></br>

## Concepts Needed
### Prime Numbers 🧮
- Understanding what prime numbers are.
- Efficient algorithms for identifying prime numbers within a range.
<br></br>
### Sieve of Eratosthenes 🏺
- An efficient algorithm for finding all prime numbers up to any given limit, which can be particularly useful for this task.
<br></br>
### Game Theory 🎲
- Basic principles of competitive games where players take turns and the concept of optimal play.
- Understanding win conditions and strategies that lead to a win or loss.
<br></br>
### Dynamic Programming/Memoization 🧠
- Using previous results to make future calculations faster, potentially necessary for optimizing the solution for multiple rounds of the game.
<br></br>
### Python Programming 🐍
- Loops and conditional statements for implementing game logic and algorithms.
- Arrays and lists for storing the integers and tracking removed numbers.
<br></br>
## Resources 📚
### Prime Numbers and Sieve of Eratosthenes
- Khan Academy: Prime Numbers: [Introduction to prime numbers](https://www.khanacademy.org/math/cc-fourth-grade-math/imp-factors-multiples-and-patterns/imp-prime-and-composite-numbers/v/prime-numbers)
- Sieve of Eratosthenes in Python: [A step-by-step guide to implementing the sieve algorithm in Python](https://www.geeksforgeeks.org/sieve-of-eratosthenes/)
<br></br>
### Game Theory Basics
- Game Theory Introduction: [A simple explanation of game theory and strategic decision-making](https://www.investopedia.com/terms/g/gametheory.asp)
<br></br>
### Dynamic Programming
- What Is Dynamic Programming With Python Examples: [An introduction to dynamic programming with Python examples](https://skerritt.blog/dynamic-programming/)
<br></br>
### Python Official Documentation
- Python Lists: [Managing lists in Python, useful for tracking the game state.](https://docs.python.org/3/tutorial/introduction.html#lists)
<br></br>
By grasping these concepts and making use of the recommended resources, you
will be well-equipped to approach the problem with a solid understanding of
both the mathematical and programming challenges involved. The key to success
in this project lies in applying efficient algorithms to manage the game’s
state and making optimal decisions based on the game’s rules.
<br></br>
<br></br>

## Additional Resources
- [Mock Technical Interview](https://www.youtube.com/watch?feature=shared&v=Jw2pniZCLi8)
<br></br>

## Requirements 📋
### General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable
<br></br>

## Tasks 📝
### Task 0. Prime Game 🎲
**Mandatory**

Maria and Ben are playing a game. Given a set of consecutive integers starting
from 1 up to and including `n`, they take turns choosing a prime number from
the set and removing that number and its multiples from the set. The player
that cannot make a move loses the game.

They play `x` rounds of the game, where `n` may be different for each round.
Assuming Maria always goes first and both players play optimally, determine who
the winner of each game is.

#### Prototype
```python
def isWinner(x, nums)
```
<br></br>

#### Solutions
See the [solutions](https://github.com/bshongwe/alx-interview/blob/master/0x0A-primegame/solutions/README.md) directory and documentation
- [Alternative #0](https://github.com/bshongwe/alx-interview/tree/master/0x0A-primegame/solutions/original-solution)
- [Alternative #1](https://github.com/bshongwe/alx-interview/tree/master/0x0A-primegame/solutions/solution-1)
- [Alternative #2](https://github.com/bshongwe/alx-interview/tree/master/0x0A-primegame/solutions/solution-2)

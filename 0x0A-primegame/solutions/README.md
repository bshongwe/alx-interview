# 🎲 Project: 0x0A. Prime Game
`Algorithm` `Python`

White boarding solutions/ playground
<br></br>

| Aspect               | Solution 1                                                                                              | Solution 2                                                                                              | Original Solution                                                                                       |
|----------------------|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| **Prime Generation** | Custom implementation using `rm_multiples` function to mark non-primes. 🛠️                                | Uses Sieve of Eratosthenes algorithm to mark non-primes. 🌟                                              | Uses Sieve of Eratosthenes algorithm to mark non-primes. 🌟                                              |
| **Prime Counting**   | Sum of primes up to `i`. 📊                                                                               | Counts primes using `filter` and `lambda`. 📈                                                               | Directly counts primes using list comprehension and built-in functions. ✅                                   |
| **Game Logic**       | For each `i` in `nums`, sums primes up to `i`. Ben wins if sum is even, Maria wins if odd. 🎲              | For each `n` in `nums`, counts primes up to `n`. Ben wins if count is even, Maria wins if odd. 🎯           | For each `n` in `nums`, counts primes up to `n`. Ben wins if count is even, Maria wins if odd. 🎯           |
| **Winner Decision**  | Compares total wins of Ben and Maria, returns the winner or `None` if tied. 🏆                          | Compares total wins of Ben and Maria, returns the winner or `None` if tied. 🏆                          | Compares total wins of Ben and Maria, returns the winner or `None` if tied. 🏆                          |
| **Edge Case Handling**| Checks if `x` <= 0, `nums` is `None`, and if length of `nums` matches `x`. 🛡️                          | Checks if `x` < 1 or if `nums` is empty. 🛡️                                                                 | Checks if `x` < 1 or if `nums` is empty. 🛡️                                                                 |
| **Efficiency**       | Less efficient due to custom implementation of prime marking and summing primes. ⏳                      | Efficient but uses `filter` and `lambda` which might be less performant. 🕒                                | More efficient due to direct use of list comprehension and built-in functions for counting primes. ⏱️        |
| **Readability**      | More complex due to custom implementation, harder to follow and maintain. 📘                              | Straightforward, but use of `filter` and `lambda` might reduce readability slightly. 📘                    | Straightforward, easy to understand and maintain. 📘                                                        |
| **Maintainability**  | Harder to maintain due to custom logic and complexity. 🔍                                                  | Easier to maintain but slightly less readable than original. 🔍                                            | Easiest to maintain due to clear and concise logic. 🔍                                                      |
| **Implementation**   | Uses a custom approach to remove multiples and sum primes. 🛠️                                            | Uses Sieve of Eratosthenes and `filter` to count primes. 🌟                                                | Uses Sieve of Eratosthenes and list comprehension to count primes. 🌟                                        |

### Summary:
- **Prime Generation:** Solution 2 and the Original Solution both use the efficient Sieve of Eratosthenes algorithm. Solution 1 uses a custom implementation which is less efficient.
- **Prime Counting:** The Original Solution is more efficient with its direct approach using list comprehension.
- **Game Logic and Winner Decision:** All three solutions use similar logic for determining the winner, but the Original Solution is more efficient and readable.
- **Edge Case Handling:** Solution 1 has more comprehensive checks compared to Solution 2 and the Original Solution.
- **Efficiency and Readability:** The Original Solution is the most efficient and readable, making it the easiest to maintain. Solution 1 is the least efficient and hardest to maintain due to its custom implementation.

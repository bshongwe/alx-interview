#!/usr/bin/python3
"""The minimum operations coding challenge.
"""


def minOperations(n):
    """Computes the fewest number of operations needed to result
    in exactly n H characters.

    Args:
        n (int): The desired number of H characters in the file.

    Returns:
        int: The fewest number of operations required to achieve n H characters.
             Returns 0 if it's impossible to achieve n H characters.
    """
    # Check if n is not an integer, return 0 if it's not possible
    if not isinstance(n, int):
        return 0

    # Intialise variables
    ops_count = 0
    clipboard = 0
    done = 1

    # print('H', end='')
    # Main loop to perform operations until the desired number of
    # characters is achieved
    while done < n:
        if clipboard == 0:
            # init (the first copy all and paste)
            clipboard = done
            done += clipboard
            ops_count += 2
            # print('-(11)->{}'.format('H' * done), end='')
        elif n - done > 0 and (n - done) % done == 0:
            # copy all and paste
            clipboard = done
            done += clipboard
            ops_count += 2
            # print('-(11)->{}'.format('H' * done), end='')
        elif clipboard > 0:
            # paste
            done += clipboard
            ops_count += 1
            # print('-(01)->{}'.format('H' * done), end='')
    # print('')
    # Return the total number of operations performed
    return ops_count

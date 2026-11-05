"""
largest_number.py

Recursively finds the largest number in a list, without using loops
or the built-in max() function.
"""


def largest_number(numbers):
    """
    Recursively find and return the largest number in 'numbers'.
    """
    # Base case: a list with only one element - that element is the largest
    if len(numbers) == 1:
        return numbers[0]

    # Recursive case: find the largest of the rest of the list
    largest_of_rest = largest_number(numbers[1:])

    # Compare the first element to the largest of the rest
    if numbers[0] > largest_of_rest:
        return numbers[0]
    return largest_of_rest


if __name__ == "__main__":
    print(largest_number([1, 4, 5, 3]))            # => 5
    print(largest_number([3, 1, 6, 8, 2, 4, 5]))    # => 8

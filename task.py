def check_number(number: float) -> None:
    """
    Prints 'Hello' if the input number is greater than 7.
    For numbers <= 7, prints a message indicating the number is too small.

    Args:
        num (float): The number to check
    """
    if number > 7:
        print("Hello")
    else:
        print(f"The number {number} is 7 or less")


def check_name(name: str) -> None:
    """
    Checks if the input name is 'John' (case-insensitive) and prints corresponding greeting.

    Args:
        name (str): The name to check

    Prints:
        'Hello, John' if name matches (any case), otherwise 'There is no such name'
    """
    if name.lower() == "john":
        print(f"Hello, John")
    else:
        print("There is no such name")


def filter_multiples_of_three(arr: list[float]) -> list[float]:
    """
    Filters elements of the input array, returning only those divisible by 3.

    Args:
        arr (list[float]): Input array of numbers

    Returns:
        list[float]: Array containing only elements divisible by 3
    """
    return [x for x in arr if abs(x % 3) < 1e-9] # 1e-9 (0.000000001) - Account for floating point precision


def is_balanced(input_string: str) -> bool:
    """
    Checks if a bracket sequence is balanced.
    Supports parentheses () and square brackets [].

    Args:
        input_string (str): Input string with parentheses

    Returns:
        bool: True if the sequence is correct, False otherwise
    """
    stack = []
    bracket_pairs = {')': '(', ']': '['}

    for char in input_string:
        # Opening parentheses
        if char in bracket_pairs.values():
            stack.append(char)
        # Closing parentheses
        elif char in bracket_pairs:
            if not stack:
                return False
            if stack[-1] != bracket_pairs[char]:
                return False
            # Remove the last opening bracket (found a pair)
            stack.pop()
    # True if the stack is empty (all brackets are closed)
    return not stack


def check_bracket_sequence() -> None:
    """
    Analyzes a bracket sequence problem and suggests several options for correction.

    Prints:
        - The original sequence
        - Whether it's correct
        - How to fix it if incorrect
        - The corrected sequence
    """
    original_sequence = "[((())()(())]]"
    print("\nGiven bracket sequence:", original_sequence)
    is_correct = is_balanced(original_sequence)
    print("Can this sequence be considered correct?", "Yes" if is_correct else "No")

    if not is_correct:
        print("To make it correct, you need to:")

        solution1 = "((())()(()))"
        print("\nSolution #1. Convert to all parentheses:")
        print("1. Change the first bracket '[' to '('")
        print("2. Change the last bracket ']' to ')'")
        print("Corrected sequence:", solution1)
        print("Validation:", is_balanced(solution1))

        solution2 = "[[(())()(())]]"
        print("\nSolution #2. Mixed option (square outside):")
        print("1. Change the second bracket '(' to '['")
        print("Corrected sequence:", solution2)
        print("Validation:", is_balanced(solution2))

        solution3 = "[((())()(()))]"
        print("\nSolution #3. Mixed option (square outside):")
        print("1. Change the second to last bracket ']' to ')'")
        print("Corrected sequence:", solution3)
        print("Validation:", is_balanced(solution3))


def main():
    """
    Main function that runs all task components interactively.

    Handles:
        1. Number comparison (>7 check)
        2. Name checking ('John' verification)
        3. Array filtering (multiples of 3)
        4. Bracket sequence analysis
    """
    print("=== Task 1: Check number > 7 ===")
    try:
        number = float(input("Enter a number: "))
        check_number(number)
    except ValueError:
        print("Please enter a valid number")

    print("\n=== Task 2: Check name ===")
    name = input("Enter a name: ").strip()
    check_name(name)

    print("\n=== Task 3: Filter multiples of 3 ===")
    try:
        arr_input = input("Enter numbers separated by spaces: ")
        arr = list(map(float, arr_input.split()))
        filtered = filter_multiples_of_three(arr)
        print("Elements multiples of 3: ", filtered)
    except ValueError:
        print("Please enter valid numbers")

    print("\n=== Task 4: Bracket sequence ===")
    check_bracket_sequence()


if __name__ == "__main__":
    main()

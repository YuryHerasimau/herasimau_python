def check_number(number: float) -> None:
    """
    Prints 'Hello' if the input number is greater than 7.

    Args:
        num (float): The number to check
    """
    if number > 7:
        print("Hello")


def check_name(name: str) -> None:
    """
    Checks if the input name is 'John' and prints corresponding greeting.

    Args:
        name (str): The name to check

    Prints:
        'Hello, John' if name matches, otherwise 'There is no such name'
    """
    if name == "John":
        print(f"Hello, {name}")
    else:
        print("There is no such name")


def filter_multiples_of_three(arr: list[int]) -> list[int]:
    """
    Filters elements of the input array, returning only those divisible by 3.

    Args:
        arr (list[int]): Input array of integers

    Returns:
        list[int]: Array containing only elements divisible by 3
    """
    result = []
    for x in arr:
        if x % 3 == 0:
            result.append(x)
    return result


def check_bracket_sequence() -> None:
    """
    Analyzes a bracket sequence problem and suggests several options for correction.

    Prints:
        - The original sequence
        - Whether it's correct
        - How to fix it if incorrect
        - The corrected sequence
    """
    sequence = "[((())()(())]]"
    print("\nGiven bracket sequence:", sequence)
    print("Can this sequence be considered correct? No")
    print("To make it correct, you need to:")

    print("\nSolution #1. Convert to all parentheses:")
    print("1. Change the first bracket '[' to '('")
    print("2. Change the last bracket ']' to ')'")
    print("Corrected sequence: ((())()(()))")

    print("\nSolution #2. Mixed option (square outside):")
    print("1. Change the second bracket '(' to '['")
    print("Corrected sequence: [[(())()(())]]")

    print("\nSolution #3. Mixed option (square outside):")
    print("1. Change the second to last bracket ']' to ')'")
    print("Corrected sequence: [((())()(()))]")


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
    name = input("Enter a name: ")
    check_name(name)

    print("\n=== Task 3: Filter multiples of 3 ===")
    try:
        arr_input = input("Enter numbers separated by spaces: ")
        arr = list(map(int, arr_input.split()))
        filtered = filter_multiples_of_three(arr)
        print("Elements multiples of 3: ", filtered)
    except ValueError:
        print("Please enter valid numbers")

    print("\n=== Task 4: Bracket sequence ===")
    check_bracket_sequence()


if __name__ == "__main__":
    main()

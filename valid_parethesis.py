"""
    Given a string s containing just the characters
    '(',')',
    '{', '}'
    '[',']',
    determine if the input string is valid.

    An input string is valid if:

        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
"""

"""
    Drawing Board:

    test_input:

        "{my}(name)[is chris]" => True
        "{my(name)}{is[chris]}" => True
        "{{my name is chris})" => False

    Linearly - O(n)
    check if A == B and number of A is even

"""

def is_valid(input_str: str) -> bool:
    """
        Description:
            Checks if input string is valid based on included parethesis
        Parameters:
            s (int): Input string
        Returns:
            bool
    """
    char_count = {}
    opening_tags = set(["[", "(", "{"])
    closing_tags = set(["]", ")", "}"])
    opening_tags_set = set()
    closing_tags_set = set()
    for char in input_str:
        if char in ["{", "}", "[", "]", "(", ")"]:
            if char in opening_tags:
                opening_tags_set.discard(char)
            else:
                opening_tags_set.add(char)
    print(opening_tags_set, closing_tags_set)
    print("------------")
    return len(opening_tags_set) == len(closing_tags_set)

TEST_INPUT_1 = "{my}(name)[is chris]"
TEST_INPUT_2 = "{my(name)}{is[chris]}"
TEST_INPUT_3 = "{{my name is chris})"

ANS_1 = is_valid(TEST_INPUT_1)
ANS_2 = is_valid(TEST_INPUT_2)
ANS_3 = is_valid(TEST_INPUT_3)

print(ANS_1, ANS_2, ANS_3)

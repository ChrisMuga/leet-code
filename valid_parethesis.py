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
    if len(input_str) == 1:
        return False
    tags = {
        "{":"}",
        "[":"]",
        "(":")"
    }
    closing_tags = (["]", ")", "}"])
    expected_closing_tags = []
    str_is_valid = False
    print(list(input_str))
    if input_str[0] in closing_tags:
        return False
    for char in input_str:
        if char in tags:
            expected_closing_tags.append(tags[char])
        if char in closing_tags and len(expected_closing_tags) > 0:
            if char != expected_closing_tags.pop():
                return False
            else:
                str_is_valid = True
        else:
            str_is_valid = False
    str_is_valid = str_is_valid if len(expected_closing_tags) == 0 else False
    return str_is_valid

    print(input_str)
    print(expected_closing_tags)


TEST_INPUT_1 = "{my}(name)[is chris]"
TEST_INPUT_2 = "{my(name)}{is[chris]}"
TEST_INPUT_3 = "{{my name is chris})"
TEST_INPUT_4 = "}{"
TEST_INPUT_5 = "({{{{}}}))"
TEST_INPUT_6 = "([]"


ANS_1 = is_valid(TEST_INPUT_1)
ANS_2 = is_valid(TEST_INPUT_2)
ANS_3 = is_valid(TEST_INPUT_3)
ANS_4 = is_valid(TEST_INPUT_4)
ANS_5 = is_valid(TEST_INPUT_5)
ANS_6 = is_valid(TEST_INPUT_6)

print(ANS_1, ANS_2, ANS_3, ANS_4, ANS_5, ANS_6)
# print(ANS_5)

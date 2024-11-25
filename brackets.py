def is_correct_bracket_seq(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            if not stack or stack.pop() != bracket_map[char]:
                return False

    return len(stack) == 0


user_input = input()
print(is_correct_bracket_seq(user_input))

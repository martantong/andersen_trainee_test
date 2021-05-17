bracket_string = input('Введите скобочную последовательность: ')
stack = []
is_good = True
for i in bracket_string:
    if i in '({[':
        stack.append(i)
    elif i in ')]}':
        if not stack:
            is_good = False
            break
        open_bracket = stack.pop()
        if open_bracket == '(' and i == ')':
            continue
        if open_bracket == '{' and i == '}':
            continue
        if open_bracket == '[' and i == ']':
            continue
        is_good = False
        break
if is_good and len(stack) == 0:
    print('Эта последовательность правильная')
else:
    print('Эта неправильная последовательность')

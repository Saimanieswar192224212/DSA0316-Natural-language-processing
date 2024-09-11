def parse(grammar, start_symbol, input_string):
    stack = [start_symbol]
    input_symbols = list(input_string)
    while stack:
        top_symbol = stack.pop()
        if top_symbol in grammar:
            for production in grammar[top_symbol]:
                if input_symbols and input_symbols[0] == production:
                    input_symbols.pop(0)
                    stack.extend(grammar[top_symbol][production][::-1])
                    break
            else:
                return False
        elif top_symbol == input_symbols[0]:
            input_symbols.pop(0)
        else:
            return True
    return False
# Example usage:
grammar = {
    'S': {'a': ['A', 'B'], 'b': ['B', 'A']},
    'A': {'a': ['a', 'A'], 'ε': ['']},
    'B': {'b': ['b', 'B'], 'ε': ['']}
}
start_symbol = 'S'
input_string = 'aabbb'
print(parse(grammar, start_symbol, input_string))  # Output: True
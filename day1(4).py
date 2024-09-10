def singular_state(input, current_state):
    if input == "NOUN":
        return "SINGULAR"
    elif input == "ES":
        return "PLURAL"
    elif input == "S":
        return "PLURAL"
    elif input == "IES":
        return "PLURAL"
    else:
        raise ValueError("Invalid input")
def plural_state(input, current_state):
    if input == "NOUN":
        return "PLURAL"
    else:
        raise ValueError("Invalid input")
def transition(input, current_state, states):
    return states[current_state](input, current_state)
def generate_plural(noun, states):
    current_state = "SINGULAR"
    if noun.endswith("y"):
        current_state = transition("NOUN", current_state, states)
        current_state = transition("IES", current_state, states)
        return noun[:-1] + "ies"
    elif noun.endswith("s") or noun.endswith("x") or noun.endswith("z") or noun.endswith("sh") or noun.endswith("ch"):
        current_state = transition("NOUN", current_state, states)
        current_state = transition("ES", current_state, states)
        return noun + "es"
    else:
        current_state = transition("NOUN", current_state, states)
        current_state = transition("S", current_state, states)
        return noun + "s"
states = {
    "SINGULAR": singular_state,
    "PLURAL": plural_state,
}
print(generate_plural("bus", states))
print(generate_plural("city", states))  
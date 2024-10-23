def evaluate_rule(node, data):
    if node.type == "operand":
        return evaluate_condition(node.value, data)
    elif node.type == "operator":
        if node.value == "AND":
            return evaluate_rule(node.left, data) and evaluate_rule(node.right, data)
        elif node.value == "OR":
            return evaluate_rule(node.left, data) or evaluate_rule(node.right, data)

def evaluate_condition(condition, data):
    # Evaluate condition like 'age > 30'
    attr, op, value = parse_condition(condition)
    if op == ">":
        return data[attr] > value
    elif op == "<":
        return data[attr] < value
    elif op == "=":
        return data[attr] == value

def parse_condition(condition):
    # Parse condition like 'age > 30' into attr, op, and value
    attr, op, value = condition.split()
    value = int(value) if value.isdigit() else value.strip("'")
    return attr, op, value

class Node:
    def __init__(self, type, value=None, left=None, right=None):
        self.type = type  # "operator" (AND/OR) or "operand" (condition)
        self.value = value  # Operand value or operator
        self.left = left  # Left node (for operators)
        self.right = right  # Right node (for operators)

def create_rule(rule_string):
    tokens = tokenize_rule(rule_string)
    return build_ast(tokens)

def tokenize_rule(rule_string):
    # Split rule into tokens (simplified for now)
    return rule_string.split()

def build_ast(tokens):
    # Example rule "age > 30 AND department = 'Sales'"
    return Node("operator", value="AND",
                left=Node("operand", value="age > 30"),
                right=Node("operand", value="department = 'Sales'"))

def combine_rules(rules):
    root = None
    for rule in rules:
        rule_ast = create_rule(rule)
        if root is None:
            root = rule_ast
        else:
            # Combine using AND as the default operator
            root = Node(type="operator", value="AND", left=root, right=rule_ast)
    return root

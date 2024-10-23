import pytest
from ast_parser import create_rule, combine_rules
from evaluator import evaluate_rule

def test_create_rule():
    rule = "age > 30 AND department = 'Sales'"
    ast = create_rule(rule)
    assert ast is not None

def test_combine_rules():
    rule1 = "age > 30 AND department = 'Sales'"
    rule2 = "salary > 50000 OR experience > 5"
    combined_ast = combine_rules([rule1, rule2])
    assert combined_ast is not None

def test_evaluate_rule():
    rule = "age > 30 AND department = 'Sales'"
    ast = create_rule(rule)
    data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
    assert evaluate_rule(ast, data) == True

    data = {"age": 25, "department": "Marketing", "salary": 30000, "experience": 1}
    assert evaluate_rule(ast, data) == False

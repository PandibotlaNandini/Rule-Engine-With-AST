from flask import Flask, request, jsonify
from ast_parser import create_rule, combine_rules
from evaluator import evaluate_rule
from db import save_rule_to_db, get_rule_from_db

app = Flask(__name__)

@app.route('/create_rule', methods=['POST'])
def create_rule_api():
    rule_string = request.json.get('rule')
    ast = create_rule(rule_string)
    rule_id = save_rule_to_db(ast, rule_string)
    return jsonify({'rule_id': rule_id, 'status': 'Rule created successfully'})

@app.route('/combine_rules', methods=['POST'])
def combine_rules_api():
    rule_ids = request.json.get('rule_ids')
    rules = [get_rule_from_db(rule_id) for rule_id in rule_ids]
    combined_ast = combine_rules(rules)
    return jsonify({'combined_ast': combined_ast})

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_api():
    rule_id = request.json.get('rule_id')
    data = request.json.get('data')
    ast = get_rule_from_db(rule_id)
    result = evaluate_rule(ast, data)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)

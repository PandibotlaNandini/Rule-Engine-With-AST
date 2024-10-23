
Rule Engine With AST
=================


A straightforward three-tier rule engine application is implemented in this project, which dynamically generates, combines, and assesses rules according on user attributes such as department, age, experience, and income. Because the rules are represented by an Abstract Syntax Tree (AST), they can be created, modified, and evaluated with flexibility.

Install
-------
Recommended to install the required dependencies using the following command:

```bash

pip install -r requirements.txt

```

Tests
-----

Run the  unit tests to validate the functionality of the rule engine, such as creating rules, combining them, and evaluating user data against those rules.

To run the tests, use pytest, which is included in the requirements.txt file.

```bash

pytest tests/test_rule_engine.py

```

Usage
-----

The rule engine provides a REST API interface for creating, combining, and evaluating rules.
Here’s how you can use the provided API endpoints.


**Step 1:** Create a rule using the /create_rule endpoint.

```bash

curl -X POST http://localhost:5000/create_rule -H "Content-Type: application/json" -d '{"rule": "(age > 30 AND department = 'Sales')"}'

```

Response:

```json

{
  "rule_id": 1,
  "status": "Rule created successfully"
}

```

**Step 2:** Combine multiple rules using /combine_rules.

```bash

curl -X POST http://localhost:5000/combine_rules -H "Content-Type: application/json" -d '{"rule_ids": [1, 2]}'

```

**Step 3:** Evaluate the rule with user data using /evaluate_rule.

```bash

curl -X POST http://localhost:5000/evaluate_rule -H "Content-Type: application/json" -d '{"rule_id": 1, "data": {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}}'

```




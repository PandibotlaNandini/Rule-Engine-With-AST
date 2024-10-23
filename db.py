import sqlite3

def get_db_connection():
    conn = sqlite3.connect('rules.db')
    conn.row_factory = sqlite3.Row
    return conn

def save_rule_to_db(ast, rule_string):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO rules (rule, ast) VALUES (?, ?)', (rule_string, str(ast)))
    rule_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return rule_id

def get_rule_from_db(rule_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT ast FROM rules WHERE id = ?', (rule_id,))
    rule = cursor.fetchone()
    conn.close()
    return rule['ast']

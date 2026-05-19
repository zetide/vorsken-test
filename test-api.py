import subprocess
import os

# Command injection - OWASP API8
def run_cmd(user_input):
    os.system(user_input)
    subprocess.call(user_input, shell=True)
    subprocess.Popen(user_input, shell=True)

# Hardcoded secret - OWASP API8
password = "hardcoded_secret_123"
api_key = "sk-1234567890abcdef"

# SQL injection pattern
def get_user(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    return query

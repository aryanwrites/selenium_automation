from flask import Flask, render_template, request, redirect
import json
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    raw_links = request.form['links']
    # Convert multiline text into a list
    link_list = [link.strip() for link in raw_links.splitlines() if link.strip()]

    # Save to JSON
    with open('links.json', 'w') as f:
        json.dump({'links': link_list}, f, indent=2)

    # Optionally trigger the automation script
    subprocess.Popen(["python3", "main.py"])

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
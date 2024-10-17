from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return f'Hello, {name}! Your form has been submitted.'

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('index.html', result="Result")


@app.route('/sample_standard_deviation', methods=['GET', 'POST'])
def sample_standard_deviation():
    user_message = request.form.get('user_message')
    return f"<h1>{user_message}</h1>"


@app.route('/population_standard_deviation', methods=['GET', 'POST'])
def population_standard_deviation():
    user_message = request.form.get('user_message')
    return f"<h1>{user_message}</h1>"

@app.route('/mean', methods=['GET', 'POST'])
def mean():
    user_message = request.form.get('user_message')
    return f"<h1>{user_message}</h1>"

@app.route('/z_score', methods=['GET', 'POST'])
def z_score():
    user_message = request.form.get('user_message')
    return f"<h1>{user_message}</h1>"

@app.route('/single_linear_regression', methods=['GET', 'POST'])
def single_linear_regression():
    user_message = request.form.get('user_message')
    return f"<h1>{user_message}</h1>"

@app.route('/y_from_linear_regression', methods=['GET', 'POST'])
def y_from_linear_regression():
    user_message = request.form.get('user_message')
    return f"<h1>{user_message}</h1>"
from flask import Flask, render_template
from src.calculator_logic import calculator_logic

app = Flask(__name__)
calculator_logic = CalculatorLogic()


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/sample_standard_deviation')
def sample_standard_deviation():
    return render_template('index.html')


@app.route('/population_standard_deviation')
def population_standard_deviation():
    return render_template('index.html')


@app.route('/mean')
def mean():
    return render_template('index.html')


@app.route('/z_score')
def z_score():
    return render_template('index.html')


@app.route('/single_linear_regression')
def single_linear_regression():
    return render_template('index.html')


@app.route('/y_from_linear_regression')
def y_from_linear_regression():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug = True)
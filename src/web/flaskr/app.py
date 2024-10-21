from flask import Flask, render_template, request, redirect, url_for
from src.calculator_logic import calculator_logic as logic

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html', operation='Enter values below, then select an operation', textbox_content='')


@app.route('/sample_standard_deviation', methods=['GET', 'POST'])
def sample_standard_deviation():
    textbox_content = request.form.get('textbox_content')
    calculation = logic.compute_sample_standard_deviation(textbox_content)
    if calculation.is_successful:
        return render_template('index.html', calculation_result=calculation.result, operation=calculation.operation,
                               textbox_content=textbox_content)
    else:
        return redirect(url_for('error', error_message=calculation.error))


@app.route('/population_standard_deviation', methods=['GET', 'POST'])
def population_standard_deviation():
    textbox_content = request.form.get('textbox_content')
    calculation = logic.compute_population_standard_deviation(textbox_content)
    if calculation.is_successful:
        return render_template('index.html', calculation_result=calculation.result, operation=calculation.operation,
                               textbox_content=textbox_content)
    else:
        return redirect(url_for('error', error_message=calculation.error))


@app.route('/mean', methods=['GET', 'POST'])
def mean():
    textbox_content = request.form.get('textbox_content')
    calculation = logic.compute_mean(textbox_content)
    if calculation.is_successful:
        return render_template('index.html', calculation_result=calculation.result, operation=calculation.operation,
                               textbox_content=textbox_content)
    else:
        return redirect(url_for('error', error_message=calculation.error))


@app.route('/z_score', methods=['GET', 'POST'])
def z_score():
    textbox_content = request.form.get('textbox_content')
    calculation = logic.compute_z_score(textbox_content)
    if calculation.is_successful:
        return render_template('index.html', calculation_result=calculation.result, operation=calculation.operation,
                               textbox_content=textbox_content)
    else:
        return redirect(url_for('error', error_message=calculation.error))


@app.route('/single_linear_regression', methods=['GET', 'POST'])
def single_linear_regression():
    textbox_content = request.form.get('textbox_content')
    calculation = logic.compute_single_linear_regression(textbox_content)
    if calculation.is_successful:
        return render_template('index.html', calculation_result=calculation.result, operation=calculation.operation,
                               textbox_content=textbox_content)
    else:
        return redirect(url_for('error', error_message=calculation.error))


@app.route('/y_from_linear_regression', methods=['GET', 'POST'])
def y_from_linear_regression():
    textbox_content = request.form.get('textbox_content')
    calculation = logic.compute_y_linear_regression(textbox_content)
    if calculation.is_successful:
        return render_template('index.html', calculation_result=calculation.result, operation=calculation.operation,
                               textbox_content=textbox_content)
    else:
        return redirect(url_for('error', error_message=calculation.error))


@app.route('/error', methods=['GET', 'POST'])
def error():
    error_message = request.args.get('error_message', 'An unknown error occurred...')
    return render_template('index.html', error_message=error_message)

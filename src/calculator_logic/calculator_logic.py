import math
import re
from .calculation_result import CalculationResult

def compute_sample_standard_deviation(textbox_content):
    # preq-LOGIC-3
    try:
        if ' ' in textbox_content:
            textbox_content = re.sub(' ', '', textbox_content)

        input_list = textbox_content.replace('\r', '').split('\n')

        while '' in input_list:
            input_list.remove('')

        for row in input_list:
            if re.search('[0-9]*', row):
                raise ValueError('Non-numeric value entered')
            if ',' in row:
                raise ValueError('Sample Standard Deviation format one value per line')

        if len(input_list) == 0:
            raise ValueError('Empty List, Sample Standard Deviation format one value per line')
        elif len(input_list) == 1:
            raise ValueError('Division by Zero, Sample Standard Deviation format one value per line')

        for i in range(len(input_list)):
            input_list[i] = float(input_list[i])

        mean = sum(input_list) / len(input_list)
        sum_diff_squares = 0

        for x in input_list:
            diff_squares = (x - mean) ** 2
            sum_diff_squares += diff_squares

        stddev = math.sqrt(sum_diff_squares / (len(input_list) - 1))

        return CalculationResult(stddev, True, "Sample Standard Deviation", "")

    except ValueError as e:
        return CalculationResult(0.0, False, "", e)


def compute_population_standard_deviation(textbox_content):
    # preq-LOGIC-4
    try:
        if ' ' in textbox_content:
            textbox_content = re.sub(' ', '', textbox_content)

        input_list = textbox_content.replace('\r', '').split('\n')
        while '' in input_list:
            input_list.remove('')

        for row in input_list:
            if re.search('[0-9]*', row):
                raise ValueError('Non-numeric value entered')
            if ',' in row:
                raise ValueError('Population Standard Deviation format one value per line')

        if len(input_list) == 0:
            raise ValueError("Empty List, Population Standard Deviation format one value per line")
        elif len(input_list) == 1:
            return CalculationResult(0.0, True, "Population Standard Deviation", "")

        for i in range(len(input_list)):
            input_list[i] = float(input_list[i])

        sum_diff_squares = 0.0
        mean = sum(input_list) / len(input_list)
        for x in input_list:
            diff_squares = (x - mean) ** 2
            sum_diff_squares += diff_squares
        stddev = math.sqrt(sum_diff_squares / len(input_list))
        return CalculationResult(stddev, True, "Population Standard Deviation", "")
    except ValueError as e:
        return CalculationResult(0.0, False, "", e)


def compute_mean(textbox_content):
    # preq-LOGIC-5
    try:

        input_list = textbox_content.replace('\r', '').split('\n')
        while '' in input_list:
            input_list.remove('')

        for row in input_list:
            if ',' in row:
                raise ValueError('Entries must be separated by new lines')

        if len(input_list) == 0:
            raise ValueError("List Is Empty")

        for i in range(len(input_list)):
            input_list[i] = float(input_list[i])

        mean = sum(input_list) / len(input_list)
        return CalculationResult(mean, True, "Mean", "")
    except ValueError as e:
        return CalculationResult(0.0, False, "", "Mean format one value per line")


def compute_z_score(textbox_content):
    # preq-LOGIC-6
    try:
        if ' ' in textbox_content:
            textbox_content = re.sub(' ', '', textbox_content)

        input_list = textbox_content.replace(' ', '').split('\n')
        while '' in input_list:
            input_list.remove('')

        if len(input_list) != 1:
            raise ValueError("Z-Score format is \"value,mean,stdDev\" on one line separated by commas")

        input_list = input_list[0].split(',')
        while '' in input_list:
            input_list.remove('')

        for row in input_list:
            if re.search('[0-9]*', row):
                raise ValueError('Non-numeric value entered')

        if len(input_list) != 3:
            raise ValueError("Z-Score format is \"value,mean,stdDev\" on one line separated by commas")

        for i in range(len(input_list)):
            input_list[i] = float(input_list[i])

        if input_list[2] == 0:
            raise ValueError("Division by Zero")

        z = (input_list[0] - input_list[1]) / input_list[2]
        return CalculationResult(z, True, "Z-Score", "")
    except ValueError as e:
        return CalculationResult(0.0, False, "", e)


def compute_single_linear_regression(textbox_content):
    # preq-LOGIC-7
    # y_hat = alpha + beta * x
    # a = y_bar - beta * x_bar
    # beta = Sum((x_i - x_bar)(y_i - y_bar)) / Sum(x_i - x_bar)^2
    # x_bar = Sum(x)/n
    # y_bar = Sum(y)/n
    try:
        if ' ' in textbox_content:
            textbox_content = re.sub(' ', '', textbox_content)

        input_pairs = textbox_content.replace('\r', '').split('\n')

        while '' in input_pairs:
            input_pairs.remove('')

        if len(input_pairs) == 0:
            raise ValueError("List Is Empty")

        x_positions = []
        y_positions = []

        for pairs in input_pairs:
            pair = pairs.split(',')
            for row in pair:
                if re.search('[0-9]*', row):
                    raise ValueError('Non-numeric value entered')
            if len(pair) != 2:
                raise ValueError("Input format is two values per line, separated by comma")
            x_positions.append(float(pair[0]))
            y_positions.append(float(pair[1]))

        if len(input_pairs) == 1:
            result = f'y = 0x + {y_positions[0]}'
            return CalculationResult(result, True, "Single Linear Regression", "")

        x_bar = sum(x_positions) / len(x_positions)
        y_bar = sum(y_positions) / len(y_positions)

        top_sum = 0
        bottom_sum = 0
        for x, y in zip(x_positions, y_positions):
            top_sum += (x - x_bar) * (y - y_bar)
            bottom_sum += (x - x_bar) ** 2
        m = top_sum/bottom_sum

        b = y_bar - m * x_bar

        result = f'y = {m}x + {b}'
        return CalculationResult(result, True, "Single Linear Regression Formula:", "")
    except ValueError as e:
        return CalculationResult(0.0, False, "", e)


def compute_y_linear_regression(textbox_content):
    # preq-LOGIC-8
    try:
        if ' ' in textbox_content:
            textbox_content = re.sub(' ', '', textbox_content)

        input_list = textbox_content.replace(' ', '').split(',')
        while '' in input_list:
            input_list.remove('')

        for row in input_list:
            if re.search('[0-9]*', row):
                raise ValueError('Non-numeric value entered')

        if len(input_list) != 3:
            raise ValueError("Exactly Three Values Required")

        for i in range(len(input_list)):
            input_list[i] = float(input_list[i])

        y = (input_list[0] * input_list[1]) + input_list[2]

        result = "y = " + str(y)
        return CalculationResult(result, True, "Single Linear Regression Prediction", "")
    except ValueError as e:
        return CalculationResult(0.0, False, "", e)
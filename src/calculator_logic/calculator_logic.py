import math

from .calculation_result import CalculationResult


def compute_sample_standard_deviation(textbox_content):
    # preq-LOGIC-3
    try:
        input_list = textbox_content.replace('\r', '').split('\n')
        if '' in input_list:
            input_list.remove('')

        if len(input_list) == 0:
            raise ValueError("List Is Empty")
        elif len(input_list) == 1:
            return CalculationResult(0.0, True, "Sample Standard Deviation", "")

        for i in range(len(input_list)):
            input_list[i] = float(input_list[i])

        mean = sum(input_list) / len(input_list)
        sum_diff_squares = 0

        for x in input_list:
            diff_squares = (x - mean) ** 2
            sum_diff_squares += diff_squares

        stddev = math.sqrt(sum_diff_squares / (len(input_list) - 1))
        print(stddev)

        return CalculationResult(stddev, True, "Sample Standard Deviation", "")

    except ValueError as e:
        return CalculationResult(0.0, False, "", e)


def compute_population_standard_deviation(textbox_content):
    # preq-LOGIC-4
    try:
        input_list = textbox_content.replace('\r', '').split('\n')
        if '' in input_list:
            input_list.remove('')

        if len(input_list) == 0:
            raise ValueError("List Is Empty")
        elif len(input_list) == 1:
            raise ValueError("Not Enough Arguments")

        for i in range(len(input_list)):
            input_list[i] = float(input_list[i])

        sum_diff_squares = 0.0
        mean = sum(input_list) / len(input_list)
        for x in input_list:
            diff_squares = (x - mean) ** 2
            sum_diff_squares += diff_squares
        stddev = math.sqrt(sum_diff_squares / len(input_list) + 1)
        return CalculationResult(stddev, True, "Population Standard Deviation", "")
    except ValueError as e:
        return CalculationResult(0.0, False, "", e)


def compute_mean(textbox_content):
    # preq-LOGIC-5
    try:
        input_list = textbox_content.replace('\r', '').split('\n')
        if '' in input_list:
            input_list.remove('')

        if len(input_list) == 0:
            raise ValueError("List Is Empty")

        for i in range(len(input_list)):
            input_list[i] = float(input_list[i])

        mean = sum(input_list) / len(input_list)
        return CalculationResult(mean, True, "Mean", "")
    except ValueError as e:
        return CalculationResult(0.0, False, "", e)


def compute_z_score(textbox_content):
    # preq-LOGIC-6
    try:
        input_list = textbox_content.replace(' ', '').split(',')
        if '' in input_list:
            input_list.remove('')

        if len(input_list) != 3:
            raise ValueError("Exactly Three Values Required")

        for i in range(len(input_list)):
            input_list[i] = float(input_list[i])

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
        input_pairs = textbox_content.replace('\r', '').split('\n')
        if '' in input_pairs:
            input_pairs.remove('')

        if len(input_pairs) == 0:
            raise ValueError("List Is Empty")

        x_positions = []
        y_positions = []

        for pairs in input_pairs:
            pair = pairs.split(',')
            x_positions.append(float(pair[0]))
            y_positions.append(float(pair[1]))
        print(x_positions)
        print(y_positions)

        x_bar = sum(x_positions) / len(x_positions)
        print(x_bar)
        y_bar = sum(y_positions) / len(y_positions)
        print(y_bar)

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
        input_list = textbox_content.replace(' ', '').split(',')
        if '' in input_list:
            input_list.remove('')

        if len(input_list) != 3:
            raise ValueError("Exactly Three Values Required")

        for i in range(len(input_list)):
            input_list[i] = float(input_list[i])

        y = (input_list[0] * input_list[1]) + input_list[2]

        result = "y = " + str(y)
        return CalculationResult(result, True, "Single Linear Regression Prediction", "")
    except ValueError as e:
        return CalculationResult(0.0, False, "", e)

import math
import re
from multiprocessing.managers import Value

from .calculation_result import CalculationResult


def compute_sample_standard_deviation(textbox_content):
    # preq-LOGIC-3
    try:
        # Split lines and remove unnecessary escape characters
        input_list = textbox_content.replace('\r', '').split('\n')

        # if the list contains a non-numeric value, raise ValueError("Sample Standard Deviation format one value per line")

        # Remove empty lines
        while '' in input_list:
            input_list.remove('')

        # Error out if values are separated by commas
        for row in input_list:
            if ',' in row:
                raise ValueError('Sample Standard Deviation format one value per line')

        # Error if the input is empty
        if len(input_list) == 0:
            raise ValueError('Empty List, Sample Standard Deviation format one value per line')

        # Error if only 1 value is given
        elif len(input_list) == 1:
            raise ValueError('Division by Zero, Sample Standard Deviation format one value per line')

        # Check for non-numeric characters
        for i in range(len(input_list)):
            input_list[i] = input_list[i].strip()
            if not re.search(r'[0-9,.]+', input_list[i]):
                raise ValueError('Non-Value found, Sample Standard Deviation format one value per line')

        # Convert strings to doubles
        for i in range(len(input_list)):
            # Catch multiple values separated by spaces
            temp = input_list[i].split(' ')
            if len(temp) > 1:
                raise ValueError('Sample Standard Deviation format one value per line')
            input_list[i] = float(input_list[i])

        # Perform the calculation
        mean = sum(input_list) / len(input_list)
        sum_diff_squares = 0

        for x in input_list:
            diff_squares = (x - mean) ** 2
            sum_diff_squares += diff_squares

        stddev = math.sqrt(sum_diff_squares / (len(input_list) - 1))

        return CalculationResult(round(stddev,10), True, "Sample Standard Deviation", "")

    # Catch errors and show the error page
    except ValueError as e:
        return CalculationResult(0.0, False, "", e)


def compute_population_standard_deviation(textbox_content):
    # preq-LOGIC-4
    try:
        # Split lines and remove unnecessary escape characters
        input_list = textbox_content.replace('\r', '').split('\n')

        # Remove empty lines
        while '' in input_list:
            input_list.remove('')

        # Error out if values are separated by commas
        for row in input_list:
            if ',' in row:
                raise ValueError('Commas Used, Population Standard Deviation format one value per line')

        # Error if the input is empty
        if len(input_list) == 0:
            raise ValueError("Empty List, Population Standard Deviation format one value per line")

        # Check for non-numeric characters
        for i in range(len(input_list)):
            input_list[i] = input_list[i].strip()
            if not re.search(r'[0-9,.]+', input_list[i]):
                raise ValueError('Non-Value found, Population Standard Deviation format one value per line')

        if len(input_list) == 1:
            return CalculationResult(0.0, True, "Population Standard Deviation", "")

        # Convert strings to doubles
        for i in range(len(input_list)):
            # Catch multiple values separated by spaces
            temp = input_list[i].split(' ')
            if len(temp) > 1:
                raise ValueError('Population Standard Deviation format one value per line')
            input_list[i] = float(input_list[i])

        sum_diff_squares = 0.0
        mean = sum(input_list) / len(input_list)
        for x in input_list:
            diff_squares = (x - mean) ** 2
            sum_diff_squares += diff_squares
        stddev = math.sqrt(sum_diff_squares / len(input_list))
        return CalculationResult(round(stddev,10), True, "Population Standard Deviation", "")

    # Catch errors and show the error page
    except ValueError as e:
        return CalculationResult(0.0, False, "", e)


def compute_mean(textbox_content):
    # preq-LOGIC-5
    try:
        # Split lines and remove unnecessary escape characters
        input_list = textbox_content.replace('\r', '').split('\n')

        # Remove empty lines
        while '' in input_list:
            input_list.remove('')

        # Error out if values are separated by commas
        for row in input_list:
            if ',' in row:
                raise ValueError('Non-Value found, Mean format one value per line')

        # Error if the input is empty
        if len(input_list) == 0:
            raise ValueError("Empty List, Mean format one value per line")

        # Check for non-numeric characters
        for i in range(len(input_list)):
            input_list[i] = input_list[i].strip()
            if not re.search(r'[0-9,.]+', input_list[i]):
                raise ValueError('Non-Value found, Mean format one value per line')

        # Convert strings to doubles
        for i in range(len(input_list)):
            # Catch multiple values separated by spaces
            temp = input_list[i].split(' ')
            if len(temp) > 1:
                raise ValueError('Mean format one value per line')
            input_list[i] = float(input_list[i])

        mean = sum(input_list) / len(input_list)
        return CalculationResult(round(mean,10), True, "Mean", "")

    # Catch errors and show the error page
    except ValueError as e:
        return CalculationResult(0.0, False, "", e)


def compute_z_score(textbox_content):
    # preq-LOGIC-6
    try:
        # Split lines and remove unnecessary escape characters
        input_list = textbox_content.split('\n')

        # Remove empty lines
        while '' in input_list:
            input_list.remove('')

        # Error if the input is empty
        if len(input_list) == 0:
            raise ValueError("Empty List, Z-Score format is \"value,mean,stdDev\" on one line separated by commas")
        elif len(input_list) > 1:
            raise ValueError("Multiline Input, Z-Score format is \"value,mean,stdDev\" on one line separated by commas")

        # Split lines and remove unnecessary escape characters
        input_list = input_list[0].split(',')
        while '' in input_list:
            input_list.remove('')

        # Check for non-numeric characters
        for i in range(len(input_list)):
            input_list[i] = input_list[i].strip()
            if not re.search(r'[0-9,.]+', input_list[i]):
                raise ValueError(
                    'Non-Value found, Z-Score format is \"value,mean,stdDev\" on one line separated by commas')

        if len(input_list) != 3:
            raise ValueError("Z-Score format is \"value,mean,stdDev\" on one line separated by commas")

        # Convert strings to doubles
        for i in range(len(input_list)):
            # Catch multiple values separated by spaces
            temp = input_list[i].split(' ')
            if len(temp) > 1:
                raise ValueError('Z-Score format is \"value,mean,stdDev\" on one line separated by commas')
            input_list[i] = float(input_list[i])

        if input_list[2] == 0:
            raise ValueError(
                "Division by Zero, Z-Score format is \"value,mean,stdDev\" on one line separated by commas")

        z = (input_list[0] - input_list[1]) / input_list[2]
        return CalculationResult(round(z,10), True, "Z-Score", "")

    # Catch errors and show the error page
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
        # Split lines and remove unnecessary escape characters
        input_pairs = textbox_content.replace('\r', '').split('\n')

        # Remove empty lines
        while '' in input_pairs:
            input_pairs.remove('')

        # Error if the input is empty
        if len(input_pairs) == 0:
            raise ValueError("Empty List, Single Linear Regression format is one x,y pair per line separated by commas")

        # Check for non-numeric characters
        for i in range(len(input_pairs)):
            input_pairs[i] = input_pairs[i].strip()
            if not re.search(r'[0-9,.]+', input_pairs[i]):
                raise ValueError(
                    'Non-Value found, Single Linear Regression format is one x,y pair per line separated by commas')

        x_positions = []
        y_positions = []

        # Convert strings to doubles and separate pairs
        for pairs in input_pairs:
            pair = pairs.split(',')
            for p in range(len(pair)):
                # Catch multiple values separated by spaces
                temp = pair[p].split(' ')
                if '' in temp:
                    temp.remove('')
                if len(temp) > 1:
                    raise ValueError('Single Linear Regression format is one x,y pair per line separated by commas')
            while '' in pair:
                pair.remove('')
            if len(pair) != 2:
                raise ValueError(
                    "Missing x or y value, Single Linear Regression format is one x,y pair per line separated by commas")
            x_positions.append(float(pair[0]))
            y_positions.append(float(pair[1]))

        if len(input_pairs) == 1:
            raise ValueError(
                "More than 1 x,y pair needed, Single Linear Regression format is one x,y pair per line separated by commas")

        if all(i == x_positions[0] for i in x_positions):
            raise ValueError(
                "All Xs are same value, Single Linear Regression format is one x,y pair per line separated by commas")

        if all(i == y_positions[0] for i in y_positions):
            raise ValueError(
                "All Ys are same value, Single Linear Regression format is one x,y pair per line separated by commas")

        x_bar = sum(x_positions) / len(x_positions)
        y_bar = sum(y_positions) / len(y_positions)

        top_sum = 0
        bottom_sum = 0
        for x, y in zip(x_positions, y_positions):
            top_sum += (x - x_bar) * (y - y_bar)
            bottom_sum += (x - x_bar) ** 2
        m = top_sum / bottom_sum

        b = y_bar - m * x_bar

        result = f'y = {round(m,10)}x + {round(b,10)}'
        return CalculationResult(result, True, "Single Linear Regression Formula:", "")

    # Catch errors and show the error page
    except ValueError as e:
        return CalculationResult(0.0, False, "", e)


def compute_predict_y(textbox_content):
    # preq-LOGIC-8
    try:
        # Split lines and remove unnecessary escape characters
        input_list = textbox_content.split('\n')

        # Remove empty lines
        while '' in input_list:
            input_list.remove('')

        # Error if the input is empty
        if len(input_list) == 0:
            raise ValueError("Empty List, Y-Prediction format is \"x, m, b\" on one line separated by commas")
        elif len(input_list) > 1:
            raise ValueError("Multiline Input, Y-Prediction format is \"x, m, b\" on one line separated by commas")

        # Split lines and remove unnecessary escape characters
        input_list = input_list[0].split(',')

        # Check for non-numeric characters
        for i in range(len(input_list)):
            input_list[i] = input_list[i].strip()
            if not re.search(r'[0-9,.]+', input_list[i]):
                raise ValueError(
                    'Non-Value found, Y-Prediction format is \"x, m, b\" on one line separated by commas')

        # Error if the input is not 3 values
        if len(input_list) != 3:
            raise ValueError("Missing Value(s), Y-Prediction format is \"x, m, b\" on one line separated by commas")

        # Convert strings to doubles
        for i in range(len(input_list)):
            # Catch multiple values separated by spaces
            temp = input_list[i].split(' ')
            if len(temp) > 1:
                raise ValueError('Y-Prediction format is \"x, m, b\" on one line separated by commas')
            input_list[i] = float(input_list[i])

        y = (input_list[0] * input_list[1]) + input_list[2]

        result = "y = " + str(round(y,10))
        return CalculationResult(result, True, "Single Linear Regression Prediction", "")

    # Catch errors and show the error page
    except ValueError as e:
        return CalculationResult(0.0, False, "", e)

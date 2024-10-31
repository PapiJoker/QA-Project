import math
import re
from .calculation_result import CalculationResult


def compute_sample_standard_deviation(textbox_content):
    # preq-LOGIC-3
    try:
        # Split lines and remove unnecessary escape characters
        input_list = textbox_content.replace('\r', '').split('\n')

        # Check for non-numeric characters
        for i in range(len(input_list)):
            input_list[i] = input_list[i].strip()
            if not re.search(r'[0-9,.]+', input_list[i]):
                raise ValueError('Characters Unallowed, Sample Standard Deviation format one value per line')

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

        return CalculationResult(stddev, True, "Sample Standard Deviation", "")

    # Catch errors and show the error page
    except ValueError as e:
        return CalculationResult(0.0, False, "", e)


def compute_population_standard_deviation(textbox_content):
    # preq-LOGIC-4
    try:
        # Split lines and remove unnecessary escape characters
        input_list = textbox_content.replace('\r', '').split('\n')

        # Check for non-numeric characters
        for i in range(len(input_list)):
            input_list[i] = input_list[i].strip()
            if not re.search(r'[0-9,.]+', input_list[i]):
                raise ValueError('Characters Unallowed, Sample Standard Deviation format one value per line')

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
        elif len(input_list) == 1:
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
        return CalculationResult(stddev, True, "Population Standard Deviation", "")

    # Catch errors and show the error page
    except ValueError as e:
        return CalculationResult(0.0, False, "", e)


def compute_mean(textbox_content):
    # preq-LOGIC-5
    try:
        # Split lines and remove unnecessary escape characters
        input_list = textbox_content.replace('\r', '').split('\n')

        # Check for non-numeric characters
        for i in range(len(input_list)):
            input_list[i] = input_list[i].strip()
            if not re.search(r'[0-9,.]+', input_list[i]):
                raise ValueError('Characters Unallowed, Sample Standard Deviation format one value per line')

        # Remove empty lines
        while '' in input_list:
            input_list.remove('')

        # Error out if values are separated by commas
        for row in input_list:
            if ',' in row:
                raise ValueError('Entries must be separated by new lines')

        # Error if the input is empty
        if len(input_list) == 0:
            raise ValueError("Empty List, Mean format one value per line")

        # Convert strings to doubles
        for i in range(len(input_list)):
            # Catch multiple values separated by spaces
            temp = input_list[i].split(' ')
            if len(temp) > 1:
                raise ValueError('Mean format one value per line')
            input_list[i] = float(input_list[i])

        mean = sum(input_list) / len(input_list)
        return CalculationResult(mean, True, "Mean", "")

    # Catch errors and show the error page
    except ValueError as e:
        return CalculationResult(0.0, False, "", "Mean format one value per line")


def compute_z_score(textbox_content):
    # preq-LOGIC-6
    try:
        # Split lines and remove unnecessary escape characters
        input_list = textbox_content.replace(' ', '').split('\n')

        # Check for non-numeric characters
        for i in range(len(input_list)):
            input_list[i] = input_list[i].strip()
            if not re.search(r'[0-9,.]+', input_list[i]):
                raise ValueError('Characters Unallowed, Sample Standard Deviation format one value per line')

        # Remove empty lines
        while '' in input_list:
            input_list.remove('')

        # Error if the input is empty
        if len(input_list) != 1:
            raise ValueError("List Is Empty, Z-Score format is \"value,mean,stdDev\" on one line separated by commas")

        input_list = input_list[0].split(',')
        while '' in input_list:
            input_list.remove('')

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
            raise ValueError("Division by Zero")

        z = (input_list[0] - input_list[1]) / input_list[2]
        return CalculationResult(z, True, "Z-Score", "")

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

        # Check for non-numeric characters
        for i in range(len(input_pairs)):
            input_pairs[i] = input_pairs[i].strip()
            if not re.search(r'[0-9,.]+', input_pairs[i]):
                raise ValueError('Characters Unallowed, Sample Standard Deviation format one value per line')

        # Remove empty lines
        while '' in input_pairs:
            input_pairs.remove('')

        # Error if the input is empty
        if len(input_pairs) == 0:
            raise ValueError("List Is Empty, Single Linear Regression format is one x,y pair per line")

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
                    raise ValueError('Single Linear Regression format is two values per line, separated by comma')
            if len(pair) != 2:
                raise ValueError("Single Linear Regression format is two values per line, separated by comma")
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
        m = top_sum / bottom_sum

        b = y_bar - m * x_bar

        result = f'y = {m}x + {b}'
        return CalculationResult(result, True, "Single Linear Regression Formula:", "")

    # Catch errors and show the error page
    except ValueError as e:
        return CalculationResult(0.0, False, "", e)


def compute_y_linear_regression(textbox_content):
    # preq-LOGIC-8
    try:
        # Split lines and remove unnecessary escape characters
        input_list = textbox_content.replace(' ', '').split(',')

        # Check for non-numeric characters
        for i in range(len(input_list)):
            input_list[i] = input_list[i].strip()
            if not re.search(r'[0-9,.]+', input_list[i]):
                raise ValueError('Characters Unallowed, Sample Standard Deviation format one value per line')

        # Remove empty lines
        while '' in input_list:
            input_list.remove('')

        # Convert strings to doubles
        for i in range(len(input_list)):
            # Catch multiple values separated by spaces
            temp = input_list[i].split(' ')
            if len(temp) > 1:
                raise ValueError('Y-Regression format is \"x, m, b\" on one line separated by commas')
            input_list[i] = float(input_list[i])

        # Error if the input is not 3 values
        if len(input_list) != 3:
            raise ValueError("Y-Regression format is \"x, m, b\" on one line separated by commas")

        y = (input_list[0] * input_list[1]) + input_list[2]

        result = "y = " + str(y)
        return CalculationResult(result, True, "Single Linear Regression Prediction", "")

    # Catch errors and show the error page
    except ValueError as e:
        return CalculationResult(0.0, False, "", e)

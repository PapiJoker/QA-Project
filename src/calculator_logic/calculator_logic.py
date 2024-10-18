import math
from re import split

from .calculation_result import CalculationResult


class CalculatorLogic:
    def compute_sample_stdev(self, textbox_content):
        #preq-LOGIC-3
        try:
            stddev = 0.0
            mean = 0.0
            diff_squares = 0.0
            sum_diff_squares = 0.0

            input_list = textbox_content.replace('\r', '').split('\n')
            if '' in input_list:
                input_list.remove('')

            for i in range(len(input_list)):
                input_list[i] = float(input_list[i])

            x_bar = sum(input_list) / len(input_list)
            sum_diff_squares = 0

            for x in input_list:
                diff_squares = (x - x_bar) ** 2
                sum_diff_squares += diff_squares

            n = 1 / (len(input_list) - 1)
            stddev = math.sqrt(n * sum_diff_squares)
            print(stddev)

            return CalculationResult(stddev, True,"Sample Standard Deviation","")

        except ValueError:
            return CalculationResult(0.0,False,"","Non-number Error")

        except ZeroDivisionError:
            return CalculationResult(0.0,False,"","List is empty")

        except Exception:
            return CalculationResult(0.0,False,"","Unknown Error Occurred")


    def compute_mean(self, textbox_content):
        #preq-LOGIC-5
        mean = sum(textbox_content) / len(textbox_content)
        return CalculationResult(mean, True,"Mean","")


    def compute_population_stdev(self, textbox_content):
        #preq-LOGIC-4
        stddev = 0.0
        mean = 0.0
        diff_squares = 0.0
        sum_diff_squares = 0.0
        mean = sum(textbox_content) / len(textbox_content)
        for x in textbox_content:
            diff_squares = (x - mean) ** 2
            sum_diff_squares += diff_squares
        stddev = math.sqrt(sum_diff_squares / len(textbox_content) + 1)
        return CalculationResult(stddev, True,"Population Standard Deviation","")


    def compute_z_score(self, textbox_content):
        #preq-LOGIC-6
        z = (textbox_content[0] - textbox_content[1]) / textbox_content[2]
        return CalculationResult(z, True,"Z-Score","")


    def compute_single_lin_reg(self, textbox_content):
        #preq-LOGIC-7
        for x in textbox_content:
            pair = x.split(",")
        return CalculationResult("y=mx+b", True,"Single Linear Regression Formula:","")


    def compute_y_lin_reg(self, textbox_content):
        #preq-LOGIC-8
        y = (textbox_content[0] * textbox_content[1]) + textbox_content[2]
        result = "y = "+str(y)
        return CalculationResult(result, True,"Single Linear Regression Prediction","")
import math
from calculation_result import CalculationResult
class CalculatorLogic:
    def compute_sample_stdev(self, input_list):
        #preq-LOGIC-3
        stddev = 0.0
        mean = 0.0
        diff_squares = 0.0
        sum_diff_squares = 0.0
        mean = sum(input_list) / len(input_list)
        for x in input_list:
            diff_squares = (x - mean) ** 2
            sum_diff_squares += diff_squares
        stddev = math.sqrt(sum_diff_squares / len(input_list))
        return CalculationResult(stddev, True,"Sample Standard Deviation","")


    def compute_mean(self, input_list):
        #preq-LOGIC-5
        mean = sum(input_list) / len(input_list)
        return CalculationResult(mean, True,"Mean","")


    def compute_population_stdev(self, input_list):
        #preq-LOGIC-4
        stddev = 0.0
        mean = 0.0
        diff_squares = 0.0
        sum_diff_squares = 0.0
        mean = sum(input_list) / len(input_list)
        for x in input_list:
            diff_squares = (x - mean) ** 2
            sum_diff_squares += diff_squares
        stddev = math.sqrt(sum_diff_squares / len(input_list)+1)
        return CalculationResult(stddev, True,"Population Standard Deviation","")


    def compute_z_score(self, input_list):
        #preq-LOGIC-6
        z = (input_list[0] - input_list[1]) / input_list[2]
        return CalculationResult(z, True,"Z-Score","")


    def compute_single_lin_reg(self, input_list):
        #preq-LOGIC-7
        for x in input_list:
            pair = x.split(",")
        return CalculationResult("y=mx+b", True,"Single Linear Regression Formula:","")


    def compute_y_lin_reg(self, input_list):
        #preq-LOGIC-8
        y = (input_list[0] * input_list[1]) + input_list[2]
        result = "y = "+str(y)
        return CalculationResult(result, True,"Single Linear Regression Prediction","")
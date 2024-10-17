class CalculationResult:
    def __init__(self, result = 0.0, is_successful = False, operation = "", error= ""):
        self.result = result
        self.is_successful = is_successful
        self.operation = operation
        self.error = error
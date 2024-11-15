import pytest
from src.calculator_logic import *


"""
MethodName_StateUnderTest_ExpectedBehavior

    Method Name = The name of the method being tested. For example, Add.
    State Under Test = The state of the method you are testing. For example, TwoFloatingPointValues.
    Expected Behavior = What you expect to happen. For example, ReturnsSumOfValues.

"""


#----------------------------------------------------Sample Standard Deviation-----------------------------------------
def test_SampleStandardDeviation_EmptyList_ReturnsError():
    #preq-UNIT-TEST-2
    #Arrange
    input_data = ""
    expected = "Empty List, Sample Standard Deviation format one value per line"

    #Act
    result = compute_sample_standard_deviation(input_data)

    #Assert
    assert expected == str(result.error)

def test_SampleStandardDeviation_InvalidList_ReturnsError():
    #preq-UNIT-TEST-2
    #Arrange
    input_data = "1,2"
    expected = "Sample Standard Deviation format one value per line"

    #Act
    result = compute_sample_standard_deviation(input_data)

    #Assert
    assert expected == str(result.error)

def test_SampleStandardDeviation_OneValue_ReturnsError():
    #preq-UNIT-TEST-2
    #Arrange
    input_data = "1"
    expected = "Division by Zero, Sample Standard Deviation format one value per line"

    #Act
    result = compute_sample_standard_deviation(input_data)

    #Assert
    assert expected == str(result.error)

def test_SampleStandardDeviation_AllZeros_ReturnsZero():
    #preq-UNIT-TEST-2
    #Arrange
    input_data = "0\n0\n0\n0\n0"
    expected = 0.0

    #Act
    result = compute_sample_standard_deviation(input_data)

    #Assert
    assert expected == result.result

def test_SampleStandardDeviation_ValidList_ReturnsSampleStandDev():
    #preq-UNIT-TEST-2
    #Arrange
    input_data = "9\n6\n8\n5\n7"
    expected = 1.5811388300841898

    #Act
    result = compute_sample_standard_deviation(input_data)

    #Assert
    assert expected == result.result

def test_SampleStandardDeviation_TwoValuesSameLineSpaced_ReturnsError():
    #preq-UNIT-TEST-2
    #Arrange
    input_data = "10\n10 10\n100"
    expected = "Sample Standard Deviation format one value per line"

    #Act
    result = compute_sample_standard_deviation(input_data)

    #Assert
    assert expected == str(result.error)

def test_SampleStandardDeviation_CharInList_ReturnsError():
    #preq-UNIT-TEST-2
    #Arrange
    input_data = "Ten\n10\n100"
    expected = "Non-Value found, Sample Standard Deviation format one value per line"

    #Act
    result = compute_sample_standard_deviation(input_data)

    #Assert
    assert expected == str(result.error)
#----------------------------------------------------Population Standard Deviation-------------------------------------
def test_PopulationStandardDeviation_ValidList_ReturnsPopulationStandDev():
    #preq-UNIT-TEST-3
    #Arrange
    input_data = "9\n6\n8\n5\n7"
    expected = 1.4142135623730951

    #Act
    result = compute_population_standard_deviation(input_data)

    #Assert
    assert expected == result.result

def test_PopulationStandardDeviation_AllZeros_ReturnsZero():
    #preq-UNIT-TEST-3
    #Arrange
    input_data = "0\n0\n0\n0\n0"
    expected = 0.0

    #Act
    result = compute_population_standard_deviation(input_data)

    #Assert
    assert expected == result.result

def test_PopulationStandardDeviation_EmptyList_ReturnsError():
    #preq-UNIT-TEST-3
    #Arrange
    input_data = ""
    expected = "Empty List, Population Standard Deviation format one value per line"

    #Act
    result = compute_population_standard_deviation(input_data)

    #Assert
    assert expected == str(result.error)
def test_PopulationStandardDeviation_OneValue_ReturnsZero():
    #preq-UNIT-TEST-3
    #Arrange
    input_data = "10"
    expected = 0.0

    #Act
    result = compute_population_standard_deviation(input_data)

    #Assert
    assert expected == result.result
def test_PopulationStandardDeviation_CommaInList_ReturnsError():
    #preq-UNIT-TEST-3
    #Arrange
    input_data = "10,10"
    expected = "Commas Used, Population Standard Deviation format one value per line"

    #Act
    result = compute_population_standard_deviation(input_data)

    #Assert
    assert expected == str(result.error)

def test_PopulationStandardDeviation_TwoValuesSameLineSpaced_ReturnsError():
    #preq-UNIT-TEST-3
    #Arrange
    input_data = "10\n10 10\n100"
    expected = "Population Standard Deviation format one value per line"

    #Act
    result = compute_population_standard_deviation(input_data)

    #Assert
    assert expected == str(result.error)

def test_PopulationStandardDeviation_CharInList_ReturnsError():
    #preq-UNIT-TEST-3
    #Arrange
    input_data = "Ten\n10\n100"
    expected = "Non-Value found, Population Standard Deviation format one value per line"

    #Act
    result = compute_population_standard_deviation(input_data)

    #Assert
    assert expected == str(result.error)
#----------------------------------------------------Mean--------------------------------------------------------------
def test_Mean_ValidList_ReturnsMean():
    #preq-UNIT-TEST-4
    #Arrange
    input_data = "9\n6\n8\n5\n7"
    expected = 7.0

    #Act
    result = compute_mean(input_data)

    #Assert
    assert expected == result.result

def test_Mean_EmptyList_ReturnsError():
    #preq-UNIT-TEST-4
    #Arrange
    input_data = ""
    expected = "Empty List, Mean format one value per line"

    #Act
    result = compute_mean(input_data)

    #Assert
    assert expected == str(result.error)

def test_Mean_CommaInList_ReturnsError():
    #preq-UNIT-TEST-4
    #Arrange
    input_data = "5,\n10\n20"
    expected = "Non-Value found, Mean format one value per line"

    #Act
    result = compute_mean(input_data)

    #Assert
    assert expected == str(result.error)

def test_Mean_TwoValuesSameLineSpaced_ReturnsError():
    #preq-UNIT-TEST-4
    #Arrange
    input_data = "5 5\n10\n20"
    expected = "Mean format one value per line"

    #Act
    result = compute_mean(input_data)

    #Assert
    assert expected == str(result.error)

def test_Mean_CharInList_ReturnsError():
    #preq-UNIT-TEST-4
    #Arrange
    input_data = "5\nNine\n20"
    expected = "Non-Value found, Mean format one value per line"

    #Act
    result = compute_mean(input_data)

    #Assert
    assert expected == str(result.error)


#----------------------------------------------------Z-Score-----------------------------------------------------------
def test_ZScore_ThreeValues_ReturnsZScore():
    #preq-UNIT-TEST-5
    #Arrange
    input_data = "11.5,7,1.5811388300841898"
    expected = 2.846049894151541

    #Act
    result = compute_z_score(input_data)

    #Assert
    assert expected == result.result

def test_ZScore_MeanZero_ReturnsZScore():
    #preq-UNIT-TEST-5
    #Arrange
    input_data = "5,0,10"
    expected = 0.5

    #Act
    result = compute_z_score(input_data)

    #Assert
    assert expected == result.result

def test_ZScore_MissingValue_ReturnsError():
    #preq-UNIT-TEST-5
    #Arrange
    input_data = "5,10,"
    expected = "Z-Score format is \"value,mean,stdDev\" on one line separated by commas"

    #Act
    result = compute_z_score(input_data)

    #Assert
    assert expected == str(result.error)

def test_ZScore_stdDevZero_ReturnsError():
    #preq-UNIT-TEST-5
    #Arrange
    input_data = "5,10,0"
    expected = "Division by Zero, Z-Score format is \"value,mean,stdDev\" on one line separated by commas"

    #Act
    result = compute_z_score(input_data)

    #Assert
    assert expected == str(result.error)
def test_ZScore_EmptyList_ReturnsError():
    #preq-UNIT-TEST-5
    #Arrange
    input_data = ""
    expected = "Empty List, Z-Score format is \"value,mean,stdDev\" on one line separated by commas"

    #Act
    result = compute_z_score(input_data)

    #Assert
    assert expected == str(result.error)

def test_ZScore_TooManyValuesSpace_ReturnsError():
    #preq-UNIT-TEST-5
    #Arrange
    input_data = "2,3 3,5"
    expected = "Z-Score format is \"value,mean,stdDev\" on one line separated by commas"

    #Act
    result = compute_z_score(input_data)

    #Assert
    assert expected == str(result.error)

def test_ZScore_CharInList_ReturnsError():
    #preq-UNIT-TEST-5
    #Arrange
    input_data = "2,three,5"
    expected = "Non-Value found, Z-Score format is \"value,mean,stdDev\" on one line separated by commas"

    #Act
    result = compute_z_score(input_data)

    #Assert
    assert expected == str(result.error)

def test_ZScore_MultilineInput_ReturnsError():
    #preq-UNIT-TEST-5
    #Arrange
    input_data = '1,2,3\n1'
    expected = 'Multiline Input, Z-Score format is \"value,mean,stdDev\" on one line separated by commas'

    #Act
    result = compute_z_score(input_data)

    #Assert
    assert expected == str(result.error)
#----------------------------------------------------Simple Linear Regression------------------------------------------
def test_SingleLinearRegression_ValidList_ReturnsSLR():
    #preq-UNIT-TEST-6
    #Arrange
    input_data = ("1.47,52.21\n1.5,53.12\n1.52,54.48\n 1.55,55.84\n1.57,57.2\n 1.6,58.57\n 1.63,59.93\n 1.65,61.29"+
                  "\n1.68,63.11\n1.7,64.47\n1.73,66.28\n1.75,68.1\n1.78,69.92\n1.8,72.19\n1.83,74.46")
    expected = "y = 61.272186542110624x + -39.06195591884392"

    #Act
    result = compute_single_linear_regression(input_data)

    #Assert
    assert expected == result.result

def test_SingleLinearRegression_EmptyList_ReturnsError():
    #preq-UNIT-TEST-6
    #Arrange
    input_data = ""
    expected = "Empty List, Single Linear Regression format is one x,y pair per line separated by commas"

    #Act
    result = compute_single_linear_regression(input_data)

    #Assert
    assert expected == str(result.error)

def test_SingleLinearRegression_AllXSame_ReturnsError():
    #preq-UNIT-TEST-6
    #Arrange
    input_data = "5,10\n5,20\n5,30"
    expected = "All Xs are same value, Single Linear Regression format is one x,y pair per line separated by commas"

    #Act
    result = compute_single_linear_regression(input_data)

    #Assert
    assert expected == str(result.error)

def test_SingleLinearRegression_AllYSame_ReturnsError():
    #preq-UNIT-TEST-6
    #Arrange
    input_data = "5,10\n15,10\n50,10"
    expected = "All Ys are same value, Single Linear Regression format is one x,y pair per line separated by commas"

    #Act
    result = compute_single_linear_regression(input_data)

    #Assert
    assert expected == str(result.error)

def test_SingleLinearRegression_AllZeros_ReturnsError():
    #preq-UNIT-TEST-6
    #Arrange
    input_data = "0,0\n0,0\n0,0"
    expected = "All Xs are same value, Single Linear Regression format is one x,y pair per line separated by commas"

    #Act
    result = compute_single_linear_regression(input_data)

    #Assert
    assert expected == str(result.error)

def test_SingleLinearRegression_MissingValue_ReturnsError():
    #preq-UNIT-TEST-6
    #Arrange
    input_data = "0,1\n10,0\n20,"
    expected = "Missing x or y value, Single Linear Regression format is one x,y pair per line separated by commas"

    #Act
    result = compute_single_linear_regression(input_data)

    #Assert
    assert expected == str(result.error)

def test_SingleLinearRegression_OnePair_ReturnsError():
    #preq-UNIT-TEST-6
    #Arrange
    input_data = "0,1"
    expected = "More than 1 x,y pair needed, Single Linear Regression format is one x,y pair per line separated by commas"

    #Act
    result = compute_single_linear_regression(input_data)

    #Assert
    assert expected == str(result.error)

def test_SingleLinearRegression_TooManyValueInPair_ReturnsError():
    #preq-UNIT-TEST-6
    #Arrange
    input_data = "0,1,1 2,3"
    expected = "Single Linear Regression format is one x,y pair per line separated by commas"

    #Act
    result = compute_single_linear_regression(input_data)

    #Assert
    assert expected == str(result.error)

def test_SingleLinearRegression_CharInList_ReturnsError():
    #preq-UNIT-TEST-6
    #Arrange
    input_data = "help me im scared"
    expected = "Non-Value found, Single Linear Regression format is one x,y pair per line separated by commas"

    #Act
    result = compute_single_linear_regression(input_data)

    #Assert
    assert expected == str(result.error)
#----------------------------------------------------Predict Y from mx+b-----------------------------------------------
def test_PredictY_ValidList_ReturnsYPrediction():
    #preq-UNIT-TEST-7
    #Arrange
    input_data = "1.535,61.272186542107434,-39.06195591838656"
    expected = "y = 54.99085042374834"

    #Act
    result = compute_predict_y(input_data)

    #Assert
    assert expected == result.result

def test_PredictY_MissingValue_ReturnsError():
    #preq-UNIT-TEST-7
    #Arrange
    input_data = "1.535,61.272186542107434"
    expected = "Missing Value(s), Y-Prediction format is \"x, m, b\" on one line separated by commas"

    #Act
    result = compute_predict_y(input_data)

    #Assert
    assert expected == str(result.error)

def test_PredictY_EmptyList_ReturnsError():
    #preq-UNIT-TEST-7
    #Arrange
    input_data = ""
    expected = "Empty List, Y-Prediction format is \"x, m, b\" on one line separated by commas"

    #Act
    result = compute_predict_y(input_data)

    #Assert
    assert expected == str(result.error)

def test_PredictY_CharinList_ReturnsError():
    #preq-UNIT-TEST-7
    #Arrange
    input_data = "123,510,zero"
    expected = "Non-Value found, Y-Prediction format is \"x, m, b\" on one line separated by commas"

    #Act
    result = compute_predict_y(input_data)

    #Assert
    assert expected == str(result.error)

def test_PredictY_MultipleValuesWithinCommas_ReturnsError():
    #preq-UNIT-TEST-7
    #Arrange
    input_data = '1,2 2,3'
    expected = 'Y-Prediction format is \"x, m, b\" on one line separated by commas'

    #Act
    result = compute_predict_y(input_data)

    #Assert
    assert expected == str(result.error)

def test_PredictY_MultilineInput_ReturnsError():
    #preq-UNIT-TEST-5
    #Arrange
    input_data = '1,2,3\n1'
    expected = 'Multiline Input, Y-Prediction format is \"x, m, b\" on one line separated by commas'

    #Act
    result = compute_predict_y(input_data)

    #Assert
    assert expected == str(result.error)
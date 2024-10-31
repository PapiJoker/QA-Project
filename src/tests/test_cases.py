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
#----------------------------------------------------Population Standard Deviation-------------------------------------
def test_PopulationStandardDeviation_ValidList_ReturnsSampleStandDev():
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
def test_PopulationStandardDeviation_CommaInList_ReturnsZero():
    #preq-UNIT-TEST-3
    #Arrange
    input_data = "10"
    expected = 0.0

    #Act
    result = compute_population_standard_deviation(input_data)

    #Assert
    assert expected == result.result
#----------------------------------------------------Mean--------------------------------------------------------------

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
#----------------------------------------------------Simple Linear Regression------------------------------------------
#----------------------------------------------------Predict Y from mx+b-----------------------------------------------
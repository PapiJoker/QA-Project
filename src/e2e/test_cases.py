import re
from playwright.sync_api import Page, expect

def test_CalculatorWebUi_VerifyPageTitle_ReturnsCorrect(page: Page):
    # preq-E2E-TEST-5
    page.goto("http://127.0.0.1:5000")

    expect(page).to_have_title(re.compile("Calculator"))

def test_CalculatorWebUi_SampleStandardDeviationValidFormat_ReturnsCorrect(page: Page):
    # preq-E2E-TEST-6
    page.goto("http://127.0.0.1:5000")

    feed = '9\n2\n5\n4\n12\n7\n8\n11\n9\n3\n7\n4\n12\n5\n4\n10\n9\n6\n9\n4'

    page.get_by_label('Values').fill(feed)

    page.click('#button_sample_standard_deviation')

    expect(page.locator('#calculation_result')).to_contain_text('3.060787652326')

def test_CalculatorWebUi_PopulationStandardDeviationEmptyList_ReturnsError(page: Page):
    # preq-E2E-TEST-7
    page.goto("http://127.0.0.1:5000")

    feed = ''

    page.get_by_label('Values').fill(feed)

    page.click('#button_population_standard_deviation')

    expect(page.locator('#error_message')).to_contain_text('Empty List, Population Standard Deviation format one value per line')

def test_CalculatorWebUi_SampleStandardDeviationSingleValue_ReturnsError(page: Page):
    # preq-E2E-TEST-8
    page.goto("http://127.0.0.1:5000")

    feed = '1'

    page.get_by_label('Values').fill(feed)

    page.click('#button_sample_standard_deviation')

    expect(page.locator('#error_message')).to_contain_text('Division by Zero, Sample Standard Deviation format one value per line')

def test_CalculatorWebUi_MeanValidFormat_ReturnsCorrect(page: Page):
    # preq-E2E-TEST-9
    page.goto("http://127.0.0.1:5000")

    feed = '9\n2\n5\n4\n12\n7\n8\n11\n9\n3\n7\n4\n12\n5\n4\n10\n9\n6\n9\n4'

    page.get_by_label('Values').fill(feed)

    page.click('#button_mean')

    expect(page.locator('#calculation_result')).to_contain_text('7.0')

def test_CalculatorWebUi_ZScoreValidFormat_ReturnsCorrect(page: Page):
    # preq-E2E-TEST-10
    page.goto("http://127.0.0.1:5000")

    feed = '5.5, 7, 3.060787652326'

    page.get_by_label('Values').fill(feed)

    page.click('#button_z_score')

    # Rounding Error
    expect(page.locator('#calculation_result')).to_contain_text('-0.49007')

def test_CalculatorWebUi_SingleLinearRegressionValidFormat_ReturnsCorrect(page: Page):
    # preq-E2E-TEST-11
    page.goto("http://127.0.0.1:5000")

    feed = '5,3\n3,2\n2,15\n1,12.3\n7.5,-3\n4,5\n3,17\n4,3\n6.42,4\n34,5\n12,17\n3,-1'

    page.get_by_label('Values').fill(feed)

    page.click('#button_single_linear_regression')

    # Rounding Error
    expect(page.locator('#calculation_result')).to_contain_text('y = -0.04596x + 6.9336')

def test_CalculatorWebUi_YPredictValidFormat_ReturnsCorrect(page: Page):
    # preq-E2E-TEST-12
    page.goto("http://127.0.0.1:5000")

    feed = '6, -0.04596, 6.9336'

    page.get_by_label('Values').fill(feed)

    page.click('#button_y_from_linear_regression')

    expect(page.locator('#calculation_result')).to_contain_text('6.65784')
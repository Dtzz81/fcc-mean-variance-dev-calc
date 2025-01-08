import pytest
from source.dev_calc import std, variance, mean, max, min, sum, calculate


@pytest.fixture
def sample_list():
    return [0,1,2,3,4,5,6,7,8]


def test_mean(sample_list):
    # arrange
    #list = [0,1,2,3,4,5,6,7,8] moved to fixture
    # act
    result = mean(sample_list)
    expected_mean =[
            [3.0, 4.0, 5.0],  # convention to start with columns
            [1.0, 4.0, 7.0],
            4.0
        ]
     # assert
    assert result == expected_mean

def test_variance(sample_list):
    result = variance(sample_list)
    expected_variance =[[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667]

    assert result == expected_variance

def test_standard_deviation(sample_list):
    result = std(sample_list)
    expected_std =[[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611]

    assert result == expected_std

def test_max(sample_list):
    result = max(sample_list)
    expected_max =[[6, 7, 8], [2, 5, 8], 8]

    assert result == expected_max

def test_min(sample_list):
    result = min(sample_list)
    expected_min = [[0, 1, 2], [0, 3, 6], 0]

    assert result == expected_min

def test_sum(sample_list):
    result = sum(sample_list)
    expected_sum = [[9, 12, 15], [3, 12, 21], 36]

    assert result == expected_sum

def test_calculate():
    result = calculate(sample_list)
    expected_result = {
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}
    assert result == expected_result


# from FCC assignemt tests (converted to pytest):

# Test case 1
def test_calculate():
    actual = calculate([2,6,2,8,4,0,1,5,7])
    expected = {'mean': [[3.6666666666666665, 5.0, 3.0], [3.3333333333333335, 4.0, 4.333333333333333], 3.888888888888889],
                'variance': [[9.555555555555557, 0.6666666666666666, 8.666666666666666], [3.555555555555556, 10.666666666666666, 6.222222222222221], 6.987654320987654],
                'standard deviation': [[3.091206165165235, 0.816496580927726, 2.943920288775949], [1.8856180831641267, 3.265986323710904, 2.494438257849294], 2.6434171674156266],
                'max': [[8, 6, 7], [6, 8, 7], 8],
                'min': [[1, 4, 0], [2, 0, 1], 0],
                'sum': [[11, 15, 9], [10, 12, 13], 35]}
    assert actual == expected, "Expected different output when calling 'calculate()' with '[2,6,2,8,4,0,1,5,7]'"

# Test case 2
def test_calculate2():
    actual = calculate([9,1,5,3,3,3,2,9,0])
    expected = {'mean': [[4.666666666666667, 4.333333333333333, 2.6666666666666665], [5.0, 3.0, 3.6666666666666665], 3.888888888888889],
                'variance': [[9.555555555555555, 11.555555555555557, 4.222222222222222], [10.666666666666666, 0.0, 14.888888888888891], 9.209876543209875],
                'standard deviation': [[3.0912061651652345, 3.39934634239519, 2.0548046676563256], [3.265986323710904, 0.0, 3.8586123009300755], 3.0347778408328137],
                'max': [[9, 9, 5], [9, 3, 9], 9],
                'min': [[2, 1, 0], [1, 3, 0], 0],
                'sum': [[14, 13, 8], [15, 9, 11], 35]}
    assert actual == expected, "Expected different output when calling 'calculate()' with '[9,1,5,3,3,3,2,9,0]'"

# Test case 3: Check for error when there are fewer than nine numbers in the list
def test_calculate_with_few_digits():
    with pytest.raises(ValueError, match="List must contain nine numbers."):
        calculate([2, 6, 2, 8, 4, 0, 1])


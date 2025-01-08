from source.dev_calc import std, variance, mean, max, min, sum, calculate

def test_mean():
    # arrange
    list = [0,1,2,3,4,5,6,7,8]
    # act
    result = mean(list)
    expected_mean =[
            [3.0, 4.0, 5.0],  # convention to start with columns
            [1.0, 4.0, 7.0],
            4.0
        ]
     # assert
    assert result == expected_mean

def test_variance():
    list = [0,1,2,3,4,5,6,7,8]
    result = variance(list)
    expected_variance =[[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667]

    assert result == expected_variance

def test_standard_deviation():
    list = [0,1,2,3,4,5,6,7,8]
    result = std(list)
    expected_std =[[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611]

    assert result == expected_std

def test_max():
    list = [0,1,2,3,4,5,6,7,8]
    result = max(list)
    expected_max =[[6, 7, 8], [2, 5, 8], 8]

    assert result == expected_max

def test_min():
    list = [0,1,2,3,4,5,6,7,8]
    result = min(list)
    expected_min = [[0, 1, 2], [0, 3, 6], 0]

    assert result == expected_min

def test_sum():
    list = [0,1,2,3,4,5,6,7,8]
    result = sum(list)
    expected_sum = [[9, 12, 15], [3, 12, 21], 36]

    assert result == expected_sum

def test_calculate():
    list = [0,1,2,3,4,5,6,7,8]
    result = calculate(list)
    expected_result = {
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}
    assert result == expected_result

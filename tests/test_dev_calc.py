from source.dev_calc import std, variance, mean

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
    # arrange
    list = [0,1,2,3,4,5,6,7,8]
    # act
    result = variance(list)
    expected_variance =[[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667]
     # assert
    assert result == expected_variance

def test_standard_deviation():
    # arrange
    list = [0,1,2,3,4,5,6,7,8]
    # act
    result = std(list)
    expected_std =[[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611]
     # assert
    assert result == expected_std

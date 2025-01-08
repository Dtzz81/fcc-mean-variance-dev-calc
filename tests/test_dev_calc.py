from source.dev_calc import calculate

def test_mean():
    # arrange
    list = [0,1,2,3,4,5,6,7,8]
    # act
    result = calculate(list)
    expected =[
            [3.0, 4.0, 5.0],  # convention to start with columns
            [1.0, 4.0, 7.0],
            4.0
        ]
     # assert
    assert result == expected


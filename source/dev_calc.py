import numpy as np


def calculate(list):
    arr_list = np.array(list)
    reshaped_arr = arr_list.reshape(3, 3)
    column_mean = np.mean(reshaped_arr, axis=0)
    row_mean = np.mean(reshaped_arr, axis=1)
    flattened_mean = np.mean(reshaped_arr)
    mean = [column_mean.tolist(), row_mean.tolist(), float(flattened_mean)]
    return mean

calculate([0,1,2,3,4,5,6,7,8])

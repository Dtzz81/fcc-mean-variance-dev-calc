import numpy as np

def calculate(list):
    pass

def mean(list):
    reshaped_arr = np.array(list).reshape(3, 3)

    column_mean = np.mean(reshaped_arr, axis=0)
    row_mean = np.mean(reshaped_arr, axis=1)
    flattened_mean = np.mean(reshaped_arr)
    mean = [column_mean.tolist(), row_mean.tolist(), float(flattened_mean)]

    return mean

def variance(list):
    reshaped_arr = np.array(list).reshape(3, 3)
    column_var = np.var(reshaped_arr, axis=0)
    row_var = np.var(reshaped_arr, axis=1)
    flattened_var = np.var(reshaped_arr)
    variance = [column_var.tolist(), row_var.tolist(), float(flattened_var)]
    return variance

def std(list):
    reshaped_arr = np.array(list).reshape(3, 3)
    column_std = np.std(reshaped_arr, axis=0)
    row_std = np.std(reshaped_arr, axis=1)
    flattened_std = np.std(reshaped_arr)
    standard_variation = [column_std.tolist(), row_std.tolist(), float(flattened_std)]
    return standard_variation

calculate([0,1,2,3,4,5,6,7,8])
